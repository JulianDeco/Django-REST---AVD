import openai
import os
from googletrans import Translator
import json
from datetime import datetime
"""
INTENTAR CON VOZ
IF VOZ O TECLADO

SE PUEDE ENVIAR EN JSON TAMBIÉN
"""

translator = Translator()

def gpt3(stext):
    date = datetime.now()
    print(date)
    openai.api_key= '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'
    response = openai.Completion.create(
    engine="text-davinci-002",
    prompt=stext,
    temperature=0.8,
    max_tokens=220,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.0,
    )
    
    content = response.choices[0].text.split('.')
    StrContent = ".".join(content)
    # arreglo = content[0]
    response = StrContent.strip('\n\n')
    # content[0] = response
    A = translator.detect(response)
    if A.lang == 'es':
        print(A)
    
    
    
    date = datetime.now()
    print(date)

    return response


print(gpt3('¿Que es un cometa?'))