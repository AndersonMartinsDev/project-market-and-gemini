import requests
import os

url_raw = os.getenv("URL_BASE_MARKET")

# Essa chamada é feita diretamente a uma fonte de dados do mercado.
# No meu caso uso o metatrader5 como fonte de dados
# Como o acesso é particular simulei a chamada usando o git assim como no treinamento de python
def callToDataFont():

    result = requests.get(url_raw)

    data = result.text

    if data == None: return ""

    return data 