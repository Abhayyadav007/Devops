FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y python3 && \
    apt-get clean

WORKDIR /app

COPY index.html /app/index.html

EXPOSE 8002

CMD ["python3", "-m", "http.server", "8002"]
