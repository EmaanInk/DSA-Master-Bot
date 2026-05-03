import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv
from lessons import LESSONS, TOPIC_ORDER, LEVEL_ORDER
import subprocess
import sys
import graphviz
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

SUPPORTED_LANGUAGES = ["Python", "C++", "Java", "JavaScript", "C"]

# ─── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="DSA Master Bot",
    page_icon="🧠",
    layout="wide"
)

st.markdown("""
<style>
    .level-badge {
        padding: 2px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 600;
    }
    .beginner { background-color: #d4edda; color: #155724; }
    .intermediate { background-color: #fff3cd; color: #856404; }
    .advanced { background-color: #f8d7da; color: #721c24; }
    .practice-box {
        background-color: #f8f9fa;
        border-left: 4px solid #6c63ff;
        padding: 15px;
        border-radius: 4px;
        margin: 10px 0;
    }
</style>
""", unsafe_allow_html=True)

# ─── Session state ──────────────────────────────────────────────────────────────
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "selected_topic" not in st.session_state:
    st.session_state.selected_topic = TOPIC_ORDER[0]
if "completed_topics" not in st.session_state:
    st.session_state.completed_topics = set()
if "show_solution" not in st.session_state:
    st.session_state.show_solution = {}
if "selected_language" not in st.session_state:
    st.session_state.selected_language = "Python"

# ─── Diagram functions ──────────────────────────────────────────────────────────
def draw_array(values=[10, 20, 30, 40, 50]):
    fig, ax = plt.subplots(figsize=(8, 2))
    for i, val in enumerate(values):
        ax.add_patch(mpatches.FancyBboxPatch(
            (i, 0), 0.9, 0.9,
            boxstyle="round,pad=0.05",
            facecolor="#6c63ff22",
            edgecolor="#6c63ff",
            linewidth=2
        ))
        ax.text(i + 0.45, 0.45, str(val), ha='center', va='center',
                fontsize=14, fontweight='bold', color="#3d3d3d")
        ax.text(i + 0.45, -0.25, f"[{i}]", ha='center', va='center',
                fontsize=10, color="#888")
    ax.set_xlim(-0.1, len(values))
    ax.set_ylim(-0.5, 1.2)
    ax.axis('off')
    ax.set_title("Array — elements stored in order, accessed by index", fontsize=12, pad=10)
    st.pyplot(fig)
    plt.close()

def draw_linked_list(values=[10, 20, 30, 40]):
    fig, ax = plt.subplots(figsize=(9, 2))
    spacing = 2.2
    for i, val in enumerate(values):
        x = i * spacing
        ax.add_patch(mpatches.FancyBboxPatch(
            (x, 0.2), 1.4, 0.7,
            boxstyle="round,pad=0.05",
            facecolor="#6c63ff22",
            edgecolor="#6c63ff",
            linewidth=2
        ))
        ax.text(x + 0.7, 0.55, str(val), ha='center', va='center',
                fontsize=13, fontweight='bold', color="#3d3d3d")
        if i < len(values) - 1:
            ax.annotate("", xy=(x + spacing, 0.55), xytext=(x + 1.4, 0.55),
                        arrowprops=dict(arrowstyle="->", color="#6c63ff", lw=2))
        else:
            ax.text(x + 1.6, 0.55, "None", ha='left', va='center',
                    fontsize=11, color="#888")
    ax.set_xlim(-0.2, len(values) * spacing + 0.5)
    ax.set_ylim(-0.2, 1.2)
    ax.axis('off')
    ax.set_title("Linked List — nodes connected by pointers", fontsize=12, pad=10)
    st.pyplot(fig)
    plt.close()

def draw_stack(values=[1, 2, 3, 4]):
    fig, ax = plt.subplots(figsize=(3, 5))
    for i, val in enumerate(values):
        y = i
        color = "#6c63ff" if i == len(values) - 1 else "#6c63ff22"
        textcolor = "white" if i == len(values) - 1 else "#3d3d3d"
        ax.add_patch(mpatches.FancyBboxPatch(
            (0.1, y), 1.8, 0.85,
            boxstyle="round,pad=0.05",
            facecolor=color,
            edgecolor="#6c63ff",
            linewidth=2
        ))
        ax.text(1.0, y + 0.42, str(val), ha='center', va='center',
                fontsize=14, fontweight='bold', color=textcolor)
        if i == len(values) - 1:
            ax.text(2.1, y + 0.42, "← TOP", ha='left', va='center',
                    fontsize=10, color="#6c63ff", fontweight='bold')
    ax.set_xlim(0, 3.5)
    ax.set_ylim(-0.2, len(values) + 0.3)
    ax.axis('off')
    ax.set_title("Stack — LIFO (Last In First Out)", fontsize=12, pad=10)
    st.pyplot(fig)
    plt.close()

def draw_queue(values=["T1", "T2", "T3", "T4"]):
    fig, ax = plt.subplots(figsize=(9, 2.5))
    spacing = 2.0
    for i, val in enumerate(values):
        x = i * spacing
        is_front = i == 0
        is_back = i == len(values) - 1
        color = "#6c63ff" if is_front else "#6c63ff22"
        textcolor = "white" if is_front else "#3d3d3d"
        ax.add_patch(mpatches.FancyBboxPatch(
            (x, 0.2), 1.6, 0.7,
            boxstyle="round,pad=0.05",
            facecolor=color,
            edgecolor="#6c63ff",
            linewidth=2
        ))
        ax.text(x + 0.8, 0.55, str(val), ha='center', va='center',
                fontsize=12, fontweight='bold', color=textcolor)
        if is_front:
            ax.text(x + 0.8, 1.05, "FRONT", ha='center', fontsize=9,
                    color="#6c63ff", fontweight='bold')
        if is_back:
            ax.text(x + 0.8, 0.05, "BACK", ha='center', fontsize=9,
                    color="#888")
    ax.annotate("dequeue →", xy=(0, 0.55), xytext=(-1.5, 0.55),
                arrowprops=dict(arrowstyle="->", color="#e74c3c", lw=2),
                fontsize=10, color="#e74c3c", va='center')
    ax.annotate("← enqueue", xy=(len(values) * spacing, 0.55),
                xytext=(len(values) * spacing + 0.2, 0.55),
                fontsize=10, color="#27ae60", va='center')
    ax.set_xlim(-2, len(values) * spacing + 1.5)
    ax.set_ylim(-0.3, 1.4)
    ax.axis('off')
    ax.set_title("Queue — FIFO (First In First Out)", fontsize=12, pad=10)
    st.pyplot(fig)
    plt.close()

def draw_binary_tree():
    dot = graphviz.Digraph(comment='Binary Tree')
    dot.attr(rankdir='TB', bgcolor='transparent')
    dot.attr('node', shape='circle', style='filled',
             fillcolor='#6c63ff22', color='#6c63ff',
             fontcolor='#3d3d3d', fontsize='14', fontweight='bold')
    dot.attr('edge', color='#6c63ff', penwidth='2')
    nodes = [('1', '1'), ('2', '2'), ('3', '3'),
             ('4', '4'), ('5', '5')]
    for node_id, label in nodes:
        dot.node(node_id, label)
    edges = [('1', '2'), ('1', '3'), ('2', '4'), ('2', '5')]
    for src, dst in edges:
        dot.edge(src, dst)
    st.graphviz_chart(dot.source)

def draw_binary_search(arr=[2, 5, 8, 12, 16, 23, 38], target=23):
    fig, ax = plt.subplots(figsize=(9, 3))
    left, right = 0, len(arr) - 1
    mid = (left + right) // 2
    for i, val in enumerate(arr):
        if i == mid:
            color = "#6c63ff"
            tc = "white"
        elif i == left or i == right:
            color = "#f39c12"
            tc = "white"
        else:
            color = "#6c63ff22"
            tc = "#3d3d3d"
        ax.add_patch(mpatches.FancyBboxPatch(
            (i, 0.3), 0.9, 0.7,
            boxstyle="round,pad=0.05",
            facecolor=color,
            edgecolor="#6c63ff",
            linewidth=2
        ))
        ax.text(i + 0.45, 0.65, str(val), ha='center', va='center',
                fontsize=12, fontweight='bold', color=tc)
    ax.text(mid + 0.45, 1.15, "MID", ha='center', fontsize=9,
            color="#6c63ff", fontweight='bold')
    ax.text(left + 0.45, 1.15, "L", ha='center', fontsize=9, color="#f39c12")
    ax.text(right + 0.45, 1.15, "R", ha='center', fontsize=9, color="#f39c12")
    ax.text(4.5, -0.1, f"Target = {target} | MID value = {arr[mid]} → search right half",
            ha='center', fontsize=10, color="#555")
    ax.set_xlim(-0.2, len(arr))
    ax.set_ylim(-0.4, 1.5)
    ax.axis('off')
    ax.set_title("Binary Search — halving the search space each step", fontsize=12, pad=10)
    st.pyplot(fig)
    plt.close()

def render_diagram(diagram_type):
    st.markdown("#### Visual Diagram")
    if diagram_type == "array":
        draw_array()
    elif diagram_type == "linked_list":
        draw_linked_list()
    elif diagram_type == "stack":
        draw_stack()
    elif diagram_type == "queue":
        draw_queue()
    elif diagram_type == "binary_tree":
        draw_binary_tree()
    elif diagram_type == "binary_search":
        draw_binary_search()

# ─── Language conversion via Groq ───────────────────────────────────────────────
def convert_code_language(python_code, target_language):
    if target_language == "Python":
        return python_code
    with st.spinner(f"Converting to {target_language}..."):
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[
                {
                    "role": "system",
                    "content": f"You are a code translator. Convert the given Python code to {target_language}. Return ONLY the translated code, no explanation, no markdown backticks, just clean code."
                },
                {
                    "role": "user",
                    "content": python_code
                }
            ],
            temperature=0.1
        )
    return response.choices[0].message.content

# ─── Chat with Groq ─────────────────────────────────────────────────────────────
def chat_with_groq(user_message, topic, language):
    lesson = LESSONS[topic]
    system_prompt = f"""You are DSA Master — an expert computer science tutor helping students learn Data Structures and Algorithms.

The student is currently studying: {topic} (Level: {lesson['level']})
Their preferred programming language is: {language}

Topic overview: {lesson['explanation']}

Your rules:
- Always give code examples in {language}
- Be encouraging and patient
- Use simple analogies for complex concepts
- When showing code, format it properly
- Keep responses concise but complete
- If asked about a different DSA topic, answer it but relate it back to {topic} when possible
"""
    st.session_state.chat_history.append({
        "role": "user",
        "content": user_message
    })
    messages = [{"role": "system", "content": system_prompt}] + \
               st.session_state.chat_history[-10:]
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=messages,
        temperature=0.7,
        stream=True
    )
    full_response = ""
    placeholder = st.empty()
    for chunk in response:
        if chunk.choices[0].delta.content:
            full_response += chunk.choices[0].delta.content
            placeholder.markdown(full_response + "▌")
    placeholder.markdown(full_response)
    st.session_state.chat_history.append({
        "role": "assistant",
        "content": full_response
    })

# ─── Run code ───────────────────────────────────────────────────────────────────
def run_python_code(code):
    try:
        result = subprocess.run(
            [sys.executable, "-c", code],
            capture_output=True, text=True, timeout=10
        )
        return result.stdout, result.stderr
    except subprocess.TimeoutExpired:
        return "", "Code took too long to run (10s timeout)"
    except Exception as e:
        return "", str(e)

# ─── Sidebar ────────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("🧠 DSA Master Bot")
    st.markdown("---")

    st.markdown("#### 🌐 Language")
    selected_lang = st.selectbox(
        "Code examples in:",
        SUPPORTED_LANGUAGES,
        index=SUPPORTED_LANGUAGES.index(st.session_state.selected_language)
    )
    if selected_lang != st.session_state.selected_language:
        st.session_state.selected_language = selected_lang
        st.rerun()

    st.markdown("---")
    st.markdown("#### 📚 Topics")

    for level in LEVEL_ORDER:
        topics_in_level = [t for t in TOPIC_ORDER
                           if LESSONS[t]["level"] == level]
        if topics_in_level:
            st.markdown(f"**{level}**")
            for topic in topics_in_level:
                done = "✅ " if topic in st.session_state.completed_topics else ""
                is_active = topic == st.session_state.selected_topic
                if st.button(
                    f"{done}{topic}",
                    key=f"nav_{topic}",
                    use_container_width=True,
                    type="primary" if is_active else "secondary"
                ):
                    st.session_state.selected_topic = topic
                    st.session_state.chat_history = []
                    st.rerun()

    st.markdown("---")
    progress = len(st.session_state.completed_topics) / len(TOPIC_ORDER)
    st.markdown("#### 📈 Progress")
    st.progress(progress)
    st.caption(f"{len(st.session_state.completed_topics)}/{len(TOPIC_ORDER)} topics completed")

    if st.button("🗑️ Clear chat", use_container_width=True):
        st.session_state.chat_history = []
        st.rerun()

# ─── Main layout ────────────────────────────────────────────────────────────────
topic = st.session_state.selected_topic
lesson = LESSONS[topic]
language = st.session_state.selected_language

lesson_col, chat_col = st.columns([1.1, 0.9])

# ─── LEFT: Lesson panel ─────────────────────────────────────────────────────────
with lesson_col:
    level = lesson["level"]
    badge_class = level.lower()
    st.markdown(
        f"## {topic} "
        f'<span class="level-badge {badge_class}">{level}</span>',
        unsafe_allow_html=True
    )

    tab1, tab2, tab3, tab4 = st.tabs(["📖 Lesson", "💻 Code", "🎯 Practice", "🎨 Diagram"])

    with tab1:
        st.markdown(lesson["explanation"])
        if st.button("✅ Mark as complete", key="complete_btn"):
            st.session_state.completed_topics.add(topic)
            st.success(f"{topic} marked as complete!")

    with tab2:
        st.markdown(f"**Code example in {language}:**")
        python_code = lesson["code"].strip()
        display_code = convert_code_language(python_code, language)
        st.code(display_code, language=language.lower()
                if language != "C++" else "cpp")

        if language == "Python":
            if st.button("▶️ Run this code", key="run_btn"):
                stdout, stderr = run_python_code(python_code)
                if stdout:
                    st.success("Output:")
                    st.code(stdout)
                if stderr:
                    st.error("Error:")
                    st.code(stderr)
        else:
            st.info(f"Live execution is available for Python only. Switch to Python to run the code.")

    with tab3:
        st.markdown("### Practice Problems")
        for i, problem in enumerate(lesson["practice"]):
            st.markdown(f"**Problem {i+1}:** {problem['question']}")
            hint_key = f"hint_{topic}_{i}"
            sol_key = f"sol_{topic}_{i}"

            col1, col2 = st.columns(2)
            with col1:
                if st.button("💡 Show hint", key=hint_key):
                    st.info(problem["hint"])
            with col2:
                if st.button("✅ Show solution", key=sol_key):
                    sol = convert_code_language(
                        problem["solution"].strip(), language)
                    st.code(sol, language=language.lower()
                            if language != "C++" else "cpp")
            st.markdown("---")

    with tab4:
        render_diagram(lesson["diagram_type"])

# ─── RIGHT: Chat panel ──────────────────────────────────────────────────────────
with chat_col:
    st.markdown(f"### 💬 Ask anything about {topic}")
    st.caption(f"AI tutor · responding in {language}")

    chat_container = st.container(height=500)
    with chat_container:
        if not st.session_state.chat_history:
            st.markdown(
                f"👋 Hi! I'm your DSA tutor. Ask me anything about **{topic}** "
                f"and I'll explain it with {language} examples!"
            )
        for msg in st.session_state.chat_history:
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

    user_input = st.chat_input(f"Ask about {topic}...")
    if user_input:
        with chat_container:
            with st.chat_message("user"):
                st.markdown(user_input)
            with st.chat_message("assistant"):
                chat_with_groq(user_input, topic, language)
        st.rerun()