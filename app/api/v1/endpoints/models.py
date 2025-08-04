from fastapi import APIRouter

router = APIRouter()

@router.post("/fine-tune/image")
def fine_tune_image_model():
    # Lógica para el fine-tuning de modelos de imagen
    return {"message": "Endpoint para fine-tuning de modelos de imagen"}
