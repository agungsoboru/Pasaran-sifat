
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


bot = commands.Bot(command_prefix='^')


@bot.event
async def on_ready():
	print("Logged in as ")



@bot.command()
async def add(ctx, args2: str):

    if args2 == 'merajan':
        zodiak_syaa = 'https://socialfordesign.files.wordpress.com/2020/01/asta.jpg'
        keterangan = 'sebaiknya Tempat sembahyang karena berhubungan dengan menyembah akan di tempatkan di timur pada nomer 4 '


    elif args2 == 'dapur':
        zodiak_syaa = 'https://socialfordesign.files.wordpress.com/2020/01/asta.jpg'
        keterangan = 'sebaiknya Dapur, karena berhubungan dengan api maka dapur ditempatkan di selatan pada nomer 6,'



    elif args2 == 'sumur':
        zodiak_syaa = 'https://socialfordesign.files.wordpress.com/2020/01/asta.jpg'
        keterangan = 'sebaiknya Karena sumur menjadi sumber air maka ditempatkan di utara dimana gunung banyak berada.'



    elif args2 == 'ternak':
        zodiak_syaa = 'https://socialfordesign.files.wordpress.com/2020/01/asta.jpg'
        keterangan ='sebaiknya ternak di tempatkan pada '




    await ctx.send("sebaiknya " + args2)
    await ctx.send(zodiak_syaa)
    await ctx.send(keterangan)

    print(args2)

bot.run('masukan token bot di sini')
