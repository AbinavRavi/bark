from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel
from bark import SAMPLE_RATE, generate_audio, preload_models
from typing import List
from numpy import ndarray as np
import json

class Prompt(BaseModel):
    text: str

app = FastAPI(title="BARK ENDPOINT")

@app.post("/get_audio")
def convert2audio(text: Prompt):
    preload_models()
    prompt = text.text
    output = generate_audio(prompt)
    return {
        "prompt": prompt,
        "audio": json.dumps(output.tolist())
    }

@app.get("/health_check")
def health_check():
    return {"status":"All Ok"}