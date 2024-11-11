from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text("Привет! Я бот Agata. Чем могу помочь?")

# Обработчик текстовых сообщений
def handle_message(update, context):
    text = update.message.text
    update.message.reply_text(f"Ты написал: {text}")

def main():
    # Вставь сюда свой токен API
    import os
from dotenv import load_dotenv

load_dotenv()
updater = Updater(os.getenv("TELEGRAM_API_TOKEN"), use_context=True)


    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(MessageHandler(Filters.text, handle_message))

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
