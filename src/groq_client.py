# src/groq_client.py
from groq import Groq
from src.config import GROQ_API_KEY, DEFAULT_MODEL, DEFAULT_TEMPERATURE, DEFAULT_TOP_P, DEFAULT_MAX_TOKENS, DEFAULT_STOP_SEQUENCE

# Initialize Groq client
client = Groq(api_key=GROQ_API_KEY)


# -------- Prompt Builders --------
def build_zero_shot_prompt(code_snippet):
    return f"""
You are a professional code assistant. Generate meaningful comments for the following code snippet.

Code:
{code_snippet}
"""


