import aiohttp
import discord
from discord.ext import commands

from holyshit import Client

bot = commands.Bot(command_prefix=">", intents=discord.Intents.default())
TOKEN = "..."


@bot.command(name="slap")
async def slap(ctx: commands.Context, member: discord.Member):
    async with Client.create() as client:
        slap_img = await client.slap()
        await ctx.send(f"You slapped {member.mention}!\n{slap_img}")


@bot.command(name="kiss")
async def kiss(ctx: commands.Context, member: discord.Member):
    async with aiohttp.ClientSession() as session:
        client = Client(session=session)
        kiss_img = await client.kiss()

    await ctx.send(f"You kissed {member.mention}!\n{kiss_img}")


bot.run(TOKEN)
