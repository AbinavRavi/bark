from fastapi import FastAPI
from pydantic import BaseModel
from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav

class Prompt(BaseModel):
    text: str

# class Output(BaseModel):
#     prompt: str
#     audio: bytearray

app = FastAPI(title="BARK ENDPOINT")

@app.post("/get_audio")
def convert2audio(text: Prompt):
    preload_models()
    prompt = text.text
    output = generate_audio(prompt)
    print(type(output))
    # write_wav("test.wav", SAMPLE_RATE, output)
    return {"status":"Done"}

@app.get("/health_check")
def health_check():
    return {"status":"All Ok"}