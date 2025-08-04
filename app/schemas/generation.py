from pydantic import BaseModel, Field
from typing import Optional, List
import uuid

# Schemas para Generación de Imágenes

class ImageGenerationParameters(BaseModel):
    creativity_level: Optional[float] = Field(0.5, ge=0.0, le=1.0, description="Mapea a 'temperature' o 'stylize'")
    detail_level: Optional[int] = Field(None, description="Nivel de detalle")
    aspect_ratio: Optional[str] = Field("1:1", description="Ej: '16:9', '1:1'")
    num_outputs: Optional[int] = Field(1, ge=1, le=4, description="Número de imágenes a generar")
    seed: Optional[int] = Field(None, description="Semilla para replicabilidad")

class ImageGenerationRequest(BaseModel):
    project_id: uuid.UUID
    user_id: uuid.UUID
    prompt_text: str
    program_id: Optional[uuid.UUID] = None
    style_id: Optional[uuid.UUID] = None
    persona_id: Optional[uuid.UUID] = None
    reference_image_url: Optional[str] = None
    model_preference_id: Optional[uuid.UUID] = None
    negative_prompt_text: Optional[str] = None
    parameters: ImageGenerationParameters = Field(default_factory=ImageGenerationParameters)

class ImageGenerationResponse(BaseModel):
    generation_id: uuid.UUID
    status: str
    image_urls: List[str]
    estimated_cost: float

# Aquí añadiremos los schemas para texto y audio más adelante.
