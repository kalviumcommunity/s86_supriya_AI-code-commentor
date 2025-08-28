# s86_supriya_AI-code-commentor
# **AI Code Comment Generator**

**Description:**
AI Code Comment Generator automatically generates meaningful comments for existing code snippets. It helps developers document their code faster, improves readability, and ensures consistent coding standards across projects.

**Tech Stack:**

* **Python** – Backend and logic
* **Streamlit** – Frontend UI for code input and output
* **Groq LLM** – AI model for generating comments
* **.env** – Store API key securely

---

## **Features**

* Generate comments for any Python code snippet
* Supports **Zero-Shot**, **One-Shot**, and **Multi-Shot** prompting
* Step-by-step reasoning using **Chain of Thought Prompting**
* Adjustable **Temperature**, **Top P**, and **Top K** parameters for creativity and diversity
* Supports **Structured Output** for easy integration into documentation tools
* Logs **token usage** for each AI call

---

## **GenAI Concepts Covered**

1. Create Project Readme
2. System and User Prompt
3. Zero-Shot Prompting
4. One-Shot Prompting
5. Multi-Shot Prompting
6. Chain of Thought Prompting
7. Tokens and Tokenization
8. LLM Features (Temperature, Top P/K, Stop Sequence, Structured Output)

---

## **Installation**

1. Clone the repository:

```bash
git clone <repo-url>
cd AI-Code-Comment-Generator
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Create a `.env` file and add your Groq API key:

```
GROQ_API_KEY=your_groq_api_key_here
```

---

## **Usage**

1. Run the Streamlit app:

```bash
streamlit run app.py
```

2. Enter a **Python code snippet** in the input box.

3. Select **Prompt Type**: Zero-Shot, One-Shot, or Multi-Shot.

4. Enable **Streaming Output** (optional).

5. Click **Generate Comments** to get AI-generated comments for your code.

---

## **Sample Input / Test Cases**

* `def add(a, b): return a + b`
* `for i in range(10): print(i)`
* `class Person: def __init__(self, name): self.name = name`

---

## **Folder Structure**

```
AI-Code-Comment-Generator/
│-- .env
│-- README.md
│-- requirements.txt
│-- app.py
│-- src/
    │-- config.py
    │-- groq_client.py
    │-- utils.py
```

---

## **License**

MIT License