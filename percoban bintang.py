
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
bot = commands.Bot(command_prefix='*')


@bot.event
async def on_ready():
	print("Logged in as ")


@bot.command()
async def add(ctx, args: int, args2: str):


    #args = int("Masukkan Tanggal Lahir: ")
    #args2 = ("Masukkan Bulan Lahir(contoh: maret,april,dst.): ")
    if args2 == 'desember':
        zodiak_syaa = 'Sagittarius' if (args < 22) else 'capricorn'

    elif args2 == 'januari':
        zodiak_syaa = 'Capricorn' if (args < 20) else 'aquarius'

    elif args2 == 'februari':
        zodiak_syaa = 'Aquarius' if (args < 19) else 'pisces'

    elif args2 == 'maret':
        zodiak_syaa = 'Pisces' if (args < 21) else 'aries'

    elif args2 == 'april':
        zodiak_syaa = 'Aries' if (args < 20) else 'taurus'

    elif args2 == 'mei':
        zodiak_syaa = 'Taurus' if (args < 21) else 'gemini'
 
    elif args2 == 'juni':
        zodiak_syaa = 'Gemini' if (args < 21) else 'cancer'

    elif args2 == 'juli':
        zodiak_syaa = 'Cancer' if (args < 23) else 'leo'

    elif args2 == 'agustus':
        zodiak_syaa = 'Leo' if (args < 23) else 'virgo'

    elif args2 == 'september':
        zodiak_syaa = 'Virgo' if (args < 23) else 'libra'
        

    elif args2 == 'oktober':
        zodiak_syaa = 'Libra' if (args < 23) else 'scorpio'

    elif args2 == 'november':
        zodiak_syaa = 'scorpio' if (args < 22) else 'sagittarius'


    join = (zodiak_syaa)

    if join == "Virgo":
        cursor = connection.execute(
            " SELECT * FROM db_watak WHERE nama = 'virgo'")

        for row in cursor:
            print(row)



    await ctx.send(row)
    print(args)
    print(args2)


bot.run('masukan token bot di sini')
