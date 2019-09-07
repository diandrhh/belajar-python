from telegram.ext import Updater, CommandHandler
import datetime
import sys
sys.path.append('/home/agungtuah/Workspaces/belajar-python/')
from rumus import Rumus
from kubus import Kubus
from balok import balok
from segitiga import SegitigaSamaSisi
from lingkaran import Lingkaran
from jajargenjang import jajargenjang
import math

def setsisikubus(bot,update, args):
    sisiskubus=args[0]
    update.message.reply_text(
        'ok sisi kubus {}'.format(args[0]))

def hello(bot, update):
    update.message.reply_text(
        'Selamat datang {}'.format(update.message.from_user.first_name))

def hitungkubus(bot,update,args):
    sisi=int(args[0])
    kubus = Kubus(sisi)
    update.message.reply_text(
        'ayo hitung kubus'
        '\nsisi kubus = {}'
        '\nluas kubus adalah : {}'.format(sisi,kubus.luas())
    )

def jajargenjangX(bot,update,args):
    sisimiring=int(args[0])
    alas=int(args[1])
    tinggi=int(args[2])

    jjrgnjg = jajargenjang(sisimiring, alas, tinggi)
    update.message.reply_text(
        'ayo hitung jajar genjang'
        '\nsisi miring jajar = {}'
        '\nalas jajar = {}'
        '\ntinggi jajar = {}'
        '\nluas jajar adalah : {}'
        '\nkeliling jajar adalah : {}'.format(sisimiring, alas, tinggi, jjrgnjg.luas(), jjrgnjg.keliling())
    )
        
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
updater.dispatcher.add_handler(CommandHandler('hitungkubus', hitungkubus, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('jajargenjang', jajargenjangX, pass_args=True))
updater.dispatcher.add_handler(CommandHandler('hariini', hariini))
updater.dispatcher.add_handler(CommandHandler('start', start))



updater.start_polling()
updater.idle()