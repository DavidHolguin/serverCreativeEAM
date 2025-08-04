import os
from dotenv import load_dotenv

# Cargar las variables de entorno desde un archivo .env
load_dotenv()

class Settings:
    # Supabase
    SUPABASE_URL: str = os.getenv("SUPABASE_URL")
    SUPABASE_KEY: str = os.getenv("SUPABASE_KEY")

    # API Keys de Modelos de IA
    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY")
    GOOGLE_API_KEY: str = os.getenv("GOOGLE_API_KEY")
    STABILITY_API_KEY: str = os.getenv("STABILITY_API_KEY")
    ELEVENLABS_API_KEY: str = os.getenv("ELEVENLABS_API_KEY")

    # Configuración del proyecto
    PROJECT_NAME: str = "Servidor de IA Generativa - EAM"
    API_V1_STR: str = "/api/v1"

settings = Settings()
