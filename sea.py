from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, Application, filters

# Функция для обработки команды /start
def start_command(update: Update, context: CallbackContext) -> None:
    # Отправляем сообщение с приветствием пользователю
    update.message.reply_text('Привет!')

# Функция для обработки текстовых сообщений
def text_message(update: Update, context: CallbackContext) -> None:
    # Получаем текст сообщения, отправленного пользователем
    message_text = update.message.text
    # Отправляем пользователю его же сообщение в ответ
    update.message.reply_text(message_text)

def main() -> None:
    # Инициализация бота
    application = Application.builder().token("5818778889:AAGNDQOGIJBr4o7TVPZvFXNqFhD8egSd0Oo").build()

    # Регистрируем обработчик команды /start с функцией start_command
    application.add_handler(CommandHandler('start', start_command))

    # Обработчик сообщений
    application.add_handler(MessageHandler(filters.TEXT, handle_message))

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()