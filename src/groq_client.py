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


def build_one_shot_prompt(code_snippet):
    return f"""
You are a professional code assistant. Generate meaningful comments for the following code snippet.

Example:
Code: def add(a, b): return a + b
Comment: Adds two numbers and returns the result

Now, generate comments for this code:
{code_snippet}
"""



def build_multi_shot_prompt(code_snippet):
    return f"""
You are a professional code assistant. Generate meaningful comments for the following code snippet.

Examples:
1) Code: def add(a, b): return a + b
   Comment: Adds two numbers and returns the result
2) Code: def square(x): return x*x
   Comment: Returns the square of a number
3) Code: def greet(name): print(f"Hello, {name}")
   Comment: Prints a greeting message using the given name

Now, generate comments for this code:
{code_snippet}
"""


# -------- AI Response Function --------
def get_ai_response(prompt, stream=False):
    """
    Calls Groq LLM with prompt.
    Supports streaming if stream=True.
    Logs token usage if not streaming.
    """
    if stream:
        completion = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stream=True,
            stop=DEFAULT_STOP_SEQUENCE
        )



        response_text = ""
        for chunk in completion:
            content = chunk.choices[0].delta.content
            if content:
                print(content, end="", flush=True)
                response_text += content
        print()
        return response_text




    else:
        response = client.chat.completions.create(
            model=DEFAULT_MODEL,
            messages=[{"role": "user", "content": prompt}],
            temperature=DEFAULT_TEMPERATURE,
            max_completion_tokens=DEFAULT_MAX_TOKENS,
            top_p=DEFAULT_TOP_P,
            stop=DEFAULT_STOP_SEQUENCE
        )


            # Log token usage
        tokens_used = getattr(response.usage, "total_tokens", None)
        if tokens_used:
            print(f"Tokens used: {tokens_used}")
            

        return response.choices[0].message.content