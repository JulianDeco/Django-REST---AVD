import openai
import os
from googletrans import Translator
import json

"""
INTENTAR CON VOZ
IF VOZ O TECLADO

SE PUEDE ENVIAR EN JSON TAMBIÉN
"""

# translator = Translator()

def gpt3(stext):
    openai.api_key= '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'
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=stext,
    temperature=0.6,
    max_tokens=70,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    )
    
    content = response.choices[0].text.split('.')
    arreglo = content[0]
    response = arreglo.strip('\n\n')
    content[0] = response
    
    return content
