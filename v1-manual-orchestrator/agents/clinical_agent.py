#AQUI VA EL LLM

from openai import OpenAI
import os
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI() # CREA UNA INSTANCIA DEL CLIENTE DE OPENAI, QUE SE UTILIZARÁ PARA REALIZAR LLAMADAS A LA API DE OPENAI.

def clinical_agent():

    prompt = "Extract the medical information from the following text: 'The patient has diabetes and hypertension."
    system_prompt = """

You are a clinical orchestration agent.

Your job is to decide which tool should be executed.

You must ONLY return valid JSON.

Available tools:
- medical_extract
- risk_scoring

Output format:

{
    "tool": "tool_name",
    "reason": "short reason"
}

"""

    response = client.chat.completions.create(
        model = "gpt-4o", #ESPECIFICA EL MODELO DE LLM QUE SE UTILIZARÁ PARA GENERAR LA RESPUESTA. EN ESTE CASO, SE UTILIZA EL MODELO "GPT-4O".
        messages=[ #utlizamos few shot prompting para darle ejemplos de como debe responder el modelo, y asi guiarlo a que responda de la manera deseada.

    {
        "role": "system",
        "content": system_prompt
    },

    {
        "role": "user",
        "content": "Patient note: Patient has diabetes and hypertension."
    },

    {
        "role": "assistant",
        "content": '{"tool":"medical_extract","reason":"clinical information detected"}'
    },

    {
        "role": "user",
        "content": "Patient note: Calculate patient cardiovascular risk."
    },

    {
        "role": "assistant",
        "content": '{"tool":"risk_scoring","reason":"risk evaluation requested"}'
    },

    {
        "role": "user",
        "content": prompt
    }
]
    )
    return "invalid json"

print(clinical_agent())