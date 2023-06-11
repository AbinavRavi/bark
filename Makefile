build:
	docker build -t bark:latest .

run:
	docker run -p 8000:8000 -v ./app:/root/.cache/ bark:latest

clean:
	docker rm -f $$(docker ps -aq)
	docker rmi -f $$(docker images -aq)