# Text to Audio service

This service uses [bark](https://github.com/suno-ai/bark) for running the inference

## Downloads

The models are downloaded by the bark service the first time the service is run so if the 
container is restarted for any reason then this will be downloaded again.

## Inference output

{
    "prompt": "Input prompt",
    "audio": "Array of audio file as a json string"
}


