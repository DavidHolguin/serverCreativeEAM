from fastapi import FastAPI

app = FastAPI(
    title="Servidor de IA Generativa - EAM",
    description="API central para la generación de textos, imágenes y audios utilizando FastAPI, Langchain y Supabase.",
    version="0.1.0",
)

@app.get("/", tags=["Root"])
def read_root():
    """
    Endpoint raíz para verificar que el servidor está en funcionamiento.
    """
    return {"message": "Bienvenido al Servidor de IA Generativa de la EAM"}

# Importar y montar los routers de los diferentes endpoints.
from app.api.v1.endpoints import generation, models
from app.core.config import settings

app.include_router(generation.router, prefix=f"{settings.API_V1_STR}/generate", tags=["Generación"])
app.include_router(models.router, prefix=f"{settings.API_V1_STR}/models", tags=["Modelos"])
