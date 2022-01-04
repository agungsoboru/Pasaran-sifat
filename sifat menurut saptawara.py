
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
bot = commands.Bot(command_prefix='#')


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
pasaran = ('Pon', 'wage', 'Kliwon', 'Umanis', 'Pahing')
# array to get the date name in javanese
dino = ('Minggu', 'Senin', 'Selasa', 'Rabu', 'Kamis', 'Jumat', 'Sabtu')


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

        tupel = (dateinput.strftime('%d %B %Y')+' hari nya ' + dino[int(
            strftime(dateinput, "%w"))]+' '+pasaran[modulo]+', wuku: '+wuku_list[nm_wuku])

        #print(dateinput.strftime('%d %B %Y')+' hari nya ' +
              #dino[int(strftime(dateinput, "%w"))]+' '+pasaran[modulo]+', wuku: '+wuku_list[nm_wuku])

        join1 = (wuku_list[nm_wuku])
        dino2 = (dino[int(strftime(dateinput, "%w"))])
     











    if dino2 == "Senin":
        cursor = connection.execute(
            " SELECT * FROM db_watak WHERE nama = 'senin-soma'")

        for row in cursor:
            print(row)

    elif dino2 == "Selasa":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'selasa-angara'")
       for row in cursor:
           print(row)

    elif dino2 == "Rabu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'rabu-buda'")
       for row in cursor:
           print(row)

    elif dino2 == "Kamis":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'kamis-werespati'")
       for row in cursor:
           print(row)

##########################################################################
    elif dino2 == "Jumat":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'jumat-sukra'")
       for row in cursor:
           print(row)

    elif dino2 == "Sabtu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'paning'")
       for row in cursor:
           print(row)

    elif dino2 == "Minggu":
       cursor = connection.execute(
           " SELECT * FROM db_watak WHERE nama = 'minggu-redite'")
       for row in cursor:
           print(row)




    await ctx.send(row)



#################################################################################


bot.run('masukan token bot di sini')
