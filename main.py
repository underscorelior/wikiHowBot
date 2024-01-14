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
	content = ""
	if message.content.startswith("how") or message.content.startswith("why") or message.content.startswith("wiki") or message.content.startswith("wikihow"):
		if message.author.id != bot.user.id:
			how_to = search_wikihow(message.content, 1)[0]
			for step in how_to.steps:
				content = content + str(step.number) + " - " + step.summary + "\n"
			await message.reply(f"**Query: {message.content}** **\n\nArticle Name:** *{how_to.title}* ```\n{content}```")

bot.run(token)
