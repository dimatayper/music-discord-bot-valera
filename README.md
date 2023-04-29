# Music Discord Bot Valera
Valera - это простой Discord бот для воспроизведения музыки из YouTube, написанный на Python с использованием библиотеки discord.py и youtube-dl.

## Основные команды
 - **!join** - Заставляет бота присоединиться к голосовому каналу.
 - **!leave** - Заставляет бота покинуть голосовой канал.
 - **!play URL** - Воспроизводит музыку с указанного URL с YouTube.
 - **!pause** - Приостанавливает воспроизведение музыки.
 - **!resume** - Возобновляет воспроизведение музыки.
 - **!stop** - Останавливает воспроизведение музыки.

## Установка и запуск
 - Убедитесь, что у вас установлен Docker на вашем компьютере или сервере.
 - Cклонируйте этот репозиторий:
```bash
git clone https://github.com/yourusername/yourrepository.git
```
 - Перейдите в каталог репозитория:
```bash
cd yourrepository
```
 - Соберите Docker-образ:
```bash
docker build -t music-bot .
```
 - Запустите Docker-контейнер, указав токен вашего бота:
```bash
docker run -e BOT_TOKEN="YOUR_BOT_TOKEN" music-bot
```

 - Теперь бот готов к работе!