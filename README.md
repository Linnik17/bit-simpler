
# Telegram Crash Signal Bot

Простой Telegram-бот для аналитических сигналов по Crash/Самолётику.

## Что умеет
- отправляет сигналы в Telegram
- запускается бесплатно через GitHub Actions
- не требует VPS/хостинга

## Как запустить

### 1. Создай бота
Напиши BotFather в Telegram:
- /newbot
- получи TOKEN

### 2. Узнай свой CHAT_ID
Напиши боту любое сообщение и открой:
https://api.telegram.org/botTOKEN/getUpdates

### 3. Залей проект на GitHub

### 4. Добавь Secrets
В GitHub:
Settings → Secrets and variables → Actions

Добавь:
- BOT_TOKEN
- CHAT_ID

### 5. Включи Actions
Actions → Enable

Бот будет запускаться каждые 15 минут.
