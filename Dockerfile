FROM python:3.11-slim 

COPY . .

RUN apt-get update && apt-get install -y git && apt-get install -y libgomp1

RUN pip install -r requirements.txt

WORKDIR /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

EXPOSE 8000

