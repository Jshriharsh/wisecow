FROM python:3.11-slim

RUN apt-get update && \
    apt-get install -y fortune-mod cowsay && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app
COPY app.py /app
RUN pip install flask

EXPOSE 4499
CMD ["python", "app.py"]
