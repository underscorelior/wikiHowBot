from pywikihow import WikiHow, search_wikihow
import discord
from discord.ext import commands
import time

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="none",intents=intents)
bot.remove_command("help")

@bot.event
async def on_ready():
	print(f'Startup at: {time.ctime()}')
	await bot.change_presence(status=discord.Status.dnd,activity=discord.Game("wikiHow do I read?"))

@bot.event
async def on_message(message):
	howtos = ""
	if message.content.startswith("how") or message.content.startswith("why") or message.content.startswith("wiki") or message.content.startswith("wikihow"):
		if message.author.id == 879180266533437460:
			pass
		else:
			cringe = message.content
			max_results = 1
			how_tos = search_wikihow(cringe, max_results)
			howtoto =  how_tos[0]
			for step in range(len(howtoto.steps)):
				strep = howtoto.steps[step]
				howtos = howtos + str(strep.number) + " - " + strep.summary + "\n"
			await message.reply(f"**Query: {cringe}** **\n\nArticle Name:** *{howtoto.title}* ```\n{howtos}```")

bot.run(token)
