import os
import time
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
IA_DISPONIVEL = False

try:
    import google.generativeai as genai
    genai.configure(api_key=GEMINI_API_KEY)
    
    # Verificar se há modelos compatíveis com generateContent
    models = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
    if models:
        IA_DISPONIVEL = True
    else:
        print("Nenhum modelo compatível encontrado.")
except Exception as e:
    print(f"IA indisponível: {e}")

