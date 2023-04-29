FROM python:3.9-slim

# Установка необходимых пакетов и ffmpeg
RUN apt-get update && \
    apt-get install -y ffmpeg && \
    apt-get clean

WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

ENV BOT_TOKEN=""

CMD ["python", "music_bot.py"]
