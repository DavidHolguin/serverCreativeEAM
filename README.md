# Servidor de IA Generativa - Universidad EAM

Este proyecto implementa un backend robusto y escalable para la generación de contenido multimedia (texto, imágenes, audio) utilizando un stack tecnológico moderno.

## Stack Tecnológico

- **Backend Framework**: FastAPI
- **Orquestación de IA**: Langchain
- **Backend as a Service**: Supabase (PostgreSQL, Storage, Auth)
- **Modelos de IA**: OpenAI, Google, Stability AI, etc.

## Configuración Inicial

1.  **Clonar el repositorio**:
    ```bash
    git clone <repository-url>
    cd serverImagenes
    ```

2.  **Crear un entorno virtual**:
    ```bash
    python -m venv venv
    ```

3.  **Activar el entorno virtual**:
    - En Windows:
      ```bash
      .\venv\Scripts\activate
      ```
    - En macOS/Linux:
      ```bash
      source venv/bin/activate
      ```

4.  **Instalar dependencias**:
    ```bash
    pip install -r requirements.txt
    ```

5.  **Configurar variables de entorno**:
    - Copiar el archivo `.env.example` a `.env`.
    - Rellenar las variables con tus credenciales (Supabase URL/Key, API Keys de los modelos de IA).

6.  **Iniciar el servidor**:
    ```bash
    uvicorn app.main:app --reload
    ```

El servidor estará disponible en `http://127.0.0.1:8000`.
