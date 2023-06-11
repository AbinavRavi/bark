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

## How to run

Build the container - make build
Run the image - make run
clean the image after done - make clean


You can use postman to send the requests to 0.0.0.0:8000 which will be the port on which server is running

/get_audio - for inference from bark
/health_check - to check for health of service

