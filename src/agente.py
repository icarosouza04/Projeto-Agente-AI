from dotenv import load_dotenv

load_dotenv()

try:
    from google import genai
    import os

    # Tenta pegar a chave da API do ambiente
    API_KEY = os.getenv("GEMINI_API_KEY")

    if API_KEY:
        client = genai.Client(api_key=API_KEY)
        IA_DISPONIVEL = True
        print("✅ IA online: modelo Gemini disponível.")
    else:
        IA_DISPONIVEL = False
        print("⚠️ Nenhuma chave de API encontrada. Usando modo offline.")
except Exception as e:
    print(f"⚠️ Erro ao inicializar IA: {e}")
    IA_DISPONIVEL = False
