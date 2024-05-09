import requests
import os

url_raw = os.getenv("URL_BASE_MARKET")
url_gemini = os.getenv("URL_CALL_GEMINI")
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Essa chamada é feita diretamente a uma fonte de dados do mercado.
# No meu caso uso o metatrader5 como fonte de dados
# Como o acesso é particular simulei a chamada usando o git assim como no treinamento de python
def callToDataFont():

    result = requests.get(url_raw)

    data = result.json()

    if data == None: return ""

    return data 

def callGemini():
    result = requests.post(url_gemini,None)