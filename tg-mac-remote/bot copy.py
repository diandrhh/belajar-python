from telegram.ext import Updater, CommandHandler
import datetime

def hello(bot, update):
    update.message.reply_text(
        'Selamat datang {}'.format(update.message.from_user.first_name))

def hariini(bot, update):
    waktu = datetime.datetime.now()
    update.message.reply_text(
        'Hari ini adalah {}'.format(waktu))

def start(bot,update):
        update.message.reply_text('halo')

def what(bot,update):
    update.message.reply_text('kamu mau apaan')
        
updater = Updater('702192490:AAEpUWyOP-2FbQLGR6FBa6lVYkm79KC68f4')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('hariini', hariini))
updater.dispatcher.add_handler(CommandHandler('start', start))


updater.start_polling()
updater.idle()