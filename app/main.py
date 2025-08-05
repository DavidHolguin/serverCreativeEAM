from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Servidor de IA Generativa - EAM",
    description="API central para la generación de textos, imágenes y audios utilizando FastAPI, Langchain y Supabase.",
    version="0.1.0",
)

# Configuración de CORS
origins = [
    "https://preview--creative-eam.lovable.app",
    "https://creative-eam.lovable.app",
    "https://*.lovable.app",
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:3000",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
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
