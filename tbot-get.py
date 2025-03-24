from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
import os

# Загрузка переменных окружения
load_dotenv()

# Получение токена из переменной окружения
bot_token = os.getenv('TELEGRAM_BOT_TOKEN')

# Функция-обработчик для команды /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш Telegram бот.')

# Функция-обработчик для текстовых сообщений
def echo(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(update.message.text)

def main():
    # Вставьте сюда свой токен
    updater = Updater(bot_token)

    dispatcher = updater.dispatcher

    # Регистрация обработчиков
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    # Set commands in Telegram
    commands = [
        ('start', 'Start the bot')
    ]
    updater.bot.set_my_commands(commands)

    # Запуск бота
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
