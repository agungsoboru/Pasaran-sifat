import discord
from discord.ext import commands
from discord_buttons_plugin import *
import os

client = commands.Bot(command_prefix=commands.when_mentioned_or("yt!"))
buttons = ButtonsClient(client)

@client.event
async def on_ready():
	print(f"Logged in as {client.user}")


###

@buttons.click
async def hibutton(ctx):
	await ctx.reply(f"Hai  {ctx.member.name} silahkan masukan tanggal dan tahun untuk mencari wuku ")

@buttons.click
async def clickbutton(ctx):
	await ctx.reply(f"{ctx.member.name} hari ini wuku.")

@buttons.click
async def danger(ctx):
	await ctx.reply(f"{ctx.member}, masukan tanggal lahir dan bulan")
	
@buttons.click
async def lol(ctx):
	await ctx.reply("masukan pasaran")


@buttons.click
async def clickbutton1(ctx):
	await ctx.reply(f"{ctx.member.name} masukan saptawara.")


@buttons.click
async def bangunan(ctx):
	await ctx.reply(f"{ctx.member.name} masukan arah pintu rumah menghadap kemana contoh utara atau bangunan apa saja yang akan dibangun.")


@buttons.click
async def kosala(ctx):
	await ctx.reply(f"{ctx.member.name} masukan arah pintu rumah menghadap kemana contoh utara atau bangunan apa saja yang akan dibangun.")

###


@client.command()
async def hi(ctx):
	await buttons.send(
		content="Hey there",
		channel = ctx.channel.id,
		components = [
			ActionRow([
				Button(

					style = ButtonType().Primary,
					label = "Mencari wuku",
					custom_id = "hibutton",

				),

				Button(
					style = ButtonType().Success,
					label = "hari ini wuku",
					custom_id = "clickbutton"

				),
				Button(
					style = ButtonType().Danger,
					label = "perbintangan",
					custom_id = "danger",
				),
				Button(
					style = ButtonType().Secondary,
					label = "pasaran",
					custom_id = "lol",
				),

				Button(
					style=ButtonType().Success,
					label="saptawara",
					custom_id="clickbutton1"

				),


			])
		]
	)


@client.command()
async def hi2(ctx):
	await buttons.send(
		content="Hey there",
		channel=ctx.channel.id,
		components=[
			ActionRow([
				Button(

					style=ButtonType().Primary,
					label="asta kosala menurut pintu masuk",
					custom_id="kosala",

				),

				Button(
					style=ButtonType().Success,
					label="asta kosala kosali menurut bangunan",
					custom_id="bangunan"

				),
				


			])
		]
	)

client.run('masukan token bot di sini')

