# 🧠 DSA Master Bot

An AI-powered Data Structures & Algorithms tutor built with Python and Streamlit. Learn DSA from beginner to advanced level with structured lessons, visual diagrams, live code execution, and an AI chat assistant — all in your preferred programming language.

---

## Features
# 🧠 DSA Master Bot

An AI-powered Data Structures & Algorithms tutor built with Python and Streamlit. Learn DSA from beginner to advanced level with structured lessons, visual diagrams, live code execution, and an AI chat assistant — all in your preferred programming language.

---

## Features

- **Structured learning path** — Topics organized by level (Beginner → Intermediate → Advanced) with explanations, code examples, and practice problems
- **AI chat tutor** — Powered by Groq (LLaMA 3.3 70B), the assistant knows exactly which topic you're studying and answers in your chosen language
- **5 language support** — Code examples dynamically converted to Python, C++, Java, JavaScript, or C using AI
- **Visual diagrams** — Every data structure visualized using Matplotlib and Graphviz
- **Live code execution** — Run Python examples directly inside the app and see the output instantly
- **Progress tracking** — Mark topics as complete and track your progress across the full curriculum

---

## Topics Covered

| Topic | Level |
|-------|-------|
| Arrays | Beginner |
| Linked Lists | Beginner |
| Stacks | Beginner |
| Queues | Beginner |
| Binary Search | Intermediate |
| Binary Trees | Intermediate |

> More topics coming soon: Hash Tables, Graphs, Dynamic Programming, Sorting Algorithms

---

## Tech Stack

- **Frontend/UI** — Streamlit
- **AI/LLM** — Groq API (LLaMA 3.3 70B)
- **Diagrams** — Matplotlib, Graphviz
- **Language** — Python 3.x

---

## Getting Started

### Prerequisites
- Python 3.8+
- Graphviz installed on your system ([download here](https://graphviz.org/download/))
- A free Groq API key ([get one here](https://console.groq.com))

### Installation

```bash
# Clone the repo
git clone https://github.com/EmaanInk/DSA-Master-Bot.git
cd DSA-Master-Bot

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Install dependencies
pip install -r requirements.txt
```

### Set up your API key

Create a `.env` file in the root directory:

```
GROQ_API_KEY=your_groq_api_key_here
```

### Run the app

```bash
streamlit run app.py
```

---

## Project Structure

```
DSA-Master-Bot/
├── app.py          # Main Streamlit app — UI, diagrams, chat, code runner
├── lessons.py      # All DSA lesson content — explanations, code, practice problems
├── requirements.txt
├── .env            # Your API key (never committed to GitHub)
└── .gitignore
```

---

## Screenshots

> Coming soon

---

## What I Learned Building This

- How to structure a multi-panel Streamlit app using columns and tabs
- Using Groq's LLaMA model for streaming AI responses
- Drawing data structure diagrams with Matplotlib and Graphviz
- Dynamic code translation using LLM APIs
- Managing app state across user interactions with Streamlit session state
- Running code safely using Python's subprocess module
- Keeping API keys secure with environment variables

---

## Author

**Emaan** — CS student building AI projects from scratch.
- GitHub: [@EmaanInk](https://github.com/EmaanInk)

---

## License

MIT License — feel free to use, modify, and share.


---

