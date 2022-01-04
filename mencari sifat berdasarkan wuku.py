
from typing_extensions import ParamSpecKwargs
from discord.ext import commands

from datetime import datetime, timedelta, date
from sqlite3.dbapi2 import Date
import calendar
from datetime import date, datetime, timedelta
from sqlite3.dbapi2 import Date
import time
from strftime import strftime
import os


from discord.ext import commands
from discord_buttons_plugin import *


import asyncio
import discord
from typing import Type
import sqlite3

import discord
from discord.ext.commands import Bot
from discord.ext import commands
from strftime import strftime


from io import StringIO
import requests
from dhooks import Webhook, Embed

from threading import Thread
from time import sleep

connection = sqlite3.connect(r"wukuterbaru.db")
bot = commands.Bot(command_prefix='$')


offset = time.timezone if (time.localtime().tm_isdst == 0) else time.altzone
tz = offset / 60 / 60 * -1


dtz = 7 - int(tz)
datenow = datetime.now()
datebase = datetime.strptime('1 1 1800', '%d %m %Y')
tomorrow = datenow + timedelta(days=1)


# formula untuk mencari pasaran
def pasaran_formula(dateinput):
    datebase = datetime.strptime('1 1 1800', '%d %m %Y')

    # find the difference between now and base date, in days
    if dateinput > datebase:
        diff = dateinput - datebase
    else:
        diff = datebase - dateinput
    diffdays = diff.days

    # find the modulo by 5
    modulo = diffdays % 5
    return modulo


# formula untuk mencari weekday


# array to get the pasaran
pasaran = ('Pon', 'wage', 'Kliwon', 'Legi', 'Pahing')
# array to get the date name in javanese
dino = ('Minggu', 'Senen', 'Seloso', 'Rebo', 'Kemis', 'Jemuwah', 'Sabtu')


@bot.event
async def on_ready():
	print("Logged in as ")





@bot.command()
async def add(ctx, args: str):

    if args:
        dateinput = datetime.strptime(args, '%d-%m-%Y')
        datebase = datetime.strptime('21 5 2000', '%d %m %Y')
        rentang = dateinput - datebase
        rentang = (rentang.days)
    #base_a      = (rentang % 210) + 210
        wk_cek = rentang % 210
        nm_wuku = int(wk_cek/7)
        modulo = pasaran_formula(dateinput)
        wuku_list = ["sinta", "landep", "ukir", "Kurantil", "tolu", "gumbrek", "wariga", "warigadean", "julungwangi", "sungsang", "dunggulan", "kuningan", "langkir", "medangsia",
                     "pujut", "pahang", "klurut", "merakih", "tambir", "medangkungan", "matal", "uye", "Menail", "prangbakat", "bala", "ugu", "wayang", "kulawu", "dukut", "watugunung"]
        

        tupel = (dateinput.strftime('%d %B %Y')+' hari nya ' + dino[int(strftime(dateinput, "%w"))]+' '+pasaran[modulo]+', wuku: '+wuku_list[nm_wuku])

        print (dateinput.strftime('%d %B %Y')+' hari nya ' +dino[int(strftime(dateinput, "%w"))]+' '+pasaran[modulo]+', wuku: '+wuku_list[nm_wuku])
        join1 = (wuku_list[nm_wuku])

        pasaran1 = (pasaran[modulo])

        print (pasaran1)


    if join1 == "sinta":
        cursor = connection.execute(
            " SELECT * FROM db_watak WHERE nama = 'sinta'")

        for row in cursor:
            print(row)

    elif join1 == "landep":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'landep'")
       for row in cursor:
           print(row)

    elif join1 == "ukir":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'ukir'")
       for row in cursor:
           print(row)

    elif join1 == "kulantir":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'kulantir'")
       for row in cursor:
           print(row)

##########################################################################
    elif join1 == "tolu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'tolu'")
       for row in cursor:
           print(row)

    elif join1 == "gumbreg":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'gumbreg'")
       for row in cursor:
           print(row)

    elif join1 == "wariga":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'wariga'")
       for row in cursor:
           print(row)

    elif join1 == "warigadean":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'warigadean'")
       for row in cursor:
           print(row)

    elif join1 == "juluwangi":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'juluwangi'")
       for row in cursor:
           print(row)

    elif join1 == "sungsang":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'sungsang'")
       for row in cursor:
           print(row)
##tsdtsadastyfddasgdfahgf######
    elif join1 == "dunggulan":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'dunggulan'")
       for row in cursor:
           print(row)

    elif join1 == "kuningan":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'kuningan'")
       for row in cursor:
           print(row)

    elif join1 == "langkir":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'langkir'")
       for row in cursor:
           print(row)

    elif join1 == "medangsia":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'medangsia'")
       for row in cursor:
           print(row)

    elif join1 == "pujut":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'pujut'")


       for row in cursor:
           print(row)

    elif join1 == "pahang":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'pahang'")
       for row in cursor:
           print(row)

    elif join1 == "klurut":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'klurut'")
       for row in cursor:
           print(row)

    elif join1 == "merakih":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'merakih'")
       for row in cursor:
           print(row)

    elif join1 == "tambir":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'tambir'")
       for row in cursor:
           print(row)

    elif join1 == "medangkungan":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'medangkungan'")
       for row in cursor:
           print(row)

    elif join1 == "matal":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'matal'")
       for row in cursor:
           print(row)

    elif join1 == "uye":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'uye'")
       for row in cursor:
           print(row)

    elif join1 == "menail":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'menail'")
       for row in cursor:
           print(row)

    elif join1 == "prangbakat":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'prangbakat'")
       for row in cursor:
           print(row)

    elif join1 == "bala":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'bala'")
       for row in cursor:
           print(row)

    elif join1 == "ugu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'ugu'")
       for row in cursor:
           print(row)

    elif join1 == "wayang":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'wayang'")
       for row in cursor:
           print(row)

    elif join1 == "kalu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'kalu'")
       for row in cursor:
           print(row)

    elif join1 == "dukut":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'dukut'")
       for row in cursor:
           print(row)

    elif join1 == "watugunung":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'watugunung'")
       for row in cursor:
           print(row)

      # connection.commit()
       
#################################################################################




    await ctx.send(args)
    await ctx.send(tupel)
    await ctx.send(row)


bot.run('masukan token bot di sini')
