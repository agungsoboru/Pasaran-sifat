
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


bot = commands.Bot(command_prefix='&')


@bot.event
async def on_ready():
	print("Logged in as ")


@bot.command()
async def add(ctx,args2: str):

    if args2 == 'utara':
        zodiak_syaa = 'https://1.bp.blogspot.com/-xXwS-S8nSn0/XKG79pN_YAI/AAAAAAAABMQ/HMhzkVgqhOoFNVUJH0k-PBqtW44xYEySgCEwYBhgL/s640/Aturan%2Bpintu%2Bmasuk%2Brumah%2Bbali%2Bmenghadap%2Bke%2Butara.jpg'

    elif args2 == 'timur':
        zodiak_syaa = 'https://4.bp.blogspot.com/-iQnwbTAeQlI/XKG79BsbzcI/AAAAAAAABMY/5DoWaN5dFD8SF1g2BvXlLjlJplDXeKd9gCEwYBhgL/s640/Aturan%2Bpintu%2Bmasuk%2Brumah%2Bbali%2Bmenghadap%2Bke%2Btimur.jpg'

    elif args2 == 'selatan':
        zodiak_syaa = 'https://3.bp.blogspot.com/-UUfOvIrBLwo/XKG784qX4DI/AAAAAAAABMU/xjxqUmVLExABos9GPBL45LgV5bjb6jSmgCEwYBhgL/s640/Aturan%2Bpintu%2Bmasuk%2Brumah%2Bbali%2Bmenghadap%2Bke%2Bselatan.jpg'

    elif args2 == 'barat':
        zodiak_syaa = 'https://3.bp.blogspot.com/-UUfOvIrBLwo/XKG784qX4DI/AAAAAAAABMU/xjxqUmVLExABos9GPBL45LgV5bjb6jSmgCEwYBhgL/s640/Aturan%2Bpintu%2Bmasuk%2Brumah%2Bbali%2Bmenghadap%2Bke%2Bselatan.jpg'
    
    await ctx.send("berikut merupakan posisi pintu menghadap " +args2)
    await ctx.send(zodiak_syaa)


bot.run('masukan token bot di sini')
