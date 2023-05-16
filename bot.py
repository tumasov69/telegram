import telegram
from telegram.ext import Updater, CommandHandler

# здесь нужно вставить токен доступа вашего бота
TOKEN = 'your_bot_token_here'

# создаем объект бота
bot = telegram.Bot(token=TOKEN)

# функции-обработчики команд
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет! Я бот.")

def help(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Это справка.")

# создаем объект updater и передаем ему токен бота
updater = Updater(token=TOKEN, use_context=True)

# получаем объект диспетчера для регистрации обработчиков
dispatcher = updater.dispatcher

# регистрируем обработчики команд
dispatcher.add_handler(CommandHandler("start", start))
dispatcher.add_handler(CommandHandler("help", help))

# запускаем бота
updater.start_polling()
