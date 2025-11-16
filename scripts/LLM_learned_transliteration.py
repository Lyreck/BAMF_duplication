# For some interesting debates on small model choice: https://huggingface.co/openai/gpt-oss-20b/discussions/14

from ollama import chat
from ollama import ChatResponse

def generate(prompt, model='mistral-small3.2'):
    response = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response.message.content


def create_prompt(text, language):

    prompt = f"""
    You are an expert name and surname transliterator. Your task is to transliterate names from their original script ({language}) to Latin script.
    Your sole output will be a single string, which is the transliterated version of the input name.

    The input is: {text}.
    """

    # Prompt with lists: 
    # You will be given a list of names and a list of surnames in {language} script. For each input, provide its transliteration
    # Your output should by a simple dictionary with three keys: 'language' (with valuealways set to {language})'name_transliteration' and 'surname_transliteration',  and their corresponding values.
    # Here is the name list: {names}

    # -----
    # Here is the surname list: {surnames}

    return prompt

def run_llm(text, language="ukrainian", model="mistral-small3.2"):

    prompt = create_prompt(text, language)

    response = generate(prompt, model=model)

    return response