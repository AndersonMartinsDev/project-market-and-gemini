from client.data_market.request_client import callToDataFont
from client.gemini.gemini_ai_client import executeGeminiAi


def callDataMarket():
    return callToDataFont()

def callGemini(prompt):
    return executeGeminiAi(prompt)