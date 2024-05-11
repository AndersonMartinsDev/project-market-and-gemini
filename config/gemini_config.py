import os

def getGeminiApiKey():
    return os.getenv("GEMINI_API_KEY")

def getGeminiVersion():
    return os.getenv("GEMINI_AI_VERSION")

def getGeminiApiUrl():
    return os.getenv("URL_CALL_GEMINI")

def getSafeSettings():
    return [
                {
                    "category": "HARM_CATEGORY_HARASSMENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_HATE_SPEECH",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                    "threshold": "BLOCK_MEDIUM_AND_ABOVE"
                },
            ]
    
def getGenerationConfig():
    return {
                "temperature": 0.2,
                "top_p": 1,
                "top_k": 0,
                "max_output_tokens": 2048,
            }
    