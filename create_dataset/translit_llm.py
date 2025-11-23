from ollama import chat
from ollama import ChatResponse

def generate(prompt, model='mistral-small3.2'): #check that this model is ok for the languages we're considering ?
    response = chat(model=model, messages=[
        {
            'role': 'user',
            'content': prompt,
        },
    ])

    return response.message.content


def create_prompt(text, language):

    # TODO set system prompt ?

    prompt = f"""
    You are an expert name and surname transliterator. Your task is to transliterate names from their original script ({language}) to Latin script.
    Your sole output will be a single string, which is the transliterated version of the input name. No end ".", no remaining special character.

    The input is: {text}.
    """

    return prompt


def run_llm(text, language="ukrainian", model="mistral-small3.2"):

    prompt = create_prompt(text, language)

    return generate(prompt, model=model)