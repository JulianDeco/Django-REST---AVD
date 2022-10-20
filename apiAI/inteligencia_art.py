import openai
import os
import json
from datetime import datetime

def gpt3(stext):
    openai.api_key= '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'
    response = openai.Completion.create(
    engine="text-curie-001",
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
    
    return response



