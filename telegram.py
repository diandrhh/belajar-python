from telegram.ext import Updater, CommandHandler


def hello(bot, update):
    update.message.reply_text(
        'Hello {}'.format(update.message.from_user.first_name))


updater = Updater('702192490 : AAEpUWyOp - @fbQLGR6FBa61VYkm79KC68f4')

updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.start_polling()
updater.idle()
