from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .connectors.pdf_connector import router as pdf_router
import os

from dotenv import load_dotenv

env_file = os.getenv("ENV_FILE", ".env")  
load_dotenv(env_file)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)


app.include_router(pdf_router, prefix="/pdf", tags=["PDF-Ingestion-APIs"])

