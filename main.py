import pandas as pd
import plotly.graph_objects as go
import subprocess

from client.requests_client import *
from rules.prompt_gemini import getPromptRules


def getAiPerspective():
    
    data = callDataMarket()
    prompt = getPromptRules() 
    prompt.append("dados :"+data)
    
    gemini_return = callGemini(prompt)

    subprocess.call("cls",shell=True)
    
    print(gemini_return)

getAiPerspective()