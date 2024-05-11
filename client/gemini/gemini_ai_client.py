import google.generativeai as genai

from config.gemini_config import getGeminiApiKey
from config.gemini_config import getGeminiVersion
from config.gemini_config import getGenerationConfig
from config.gemini_config import getSafeSettings

api_key = getGeminiApiKey()
gemini_version = getGeminiVersion()
gemini_config = getGenerationConfig()
safety_settings = getSafeSettings()

genai.configure(api_key=api_key)

model = genai.GenerativeModel(model_name=gemini_version,
                              generation_config=gemini_config,
                              safety_settings=safety_settings)

def executeGeminiAi(prompt):
  response = model.generate_content(prompt)
  if response == None:
    return "Gemini não apresentou um resultado"
  else:
    return response.text