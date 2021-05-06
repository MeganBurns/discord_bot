import random
import discord
from discord.ext import commands

def setup(bot):
    bot.add_cog(my_cog(bot))

class my_cog(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='8ball')
    async def oracle(self, ctx, question: str):
        outputs = ["Yes", "No", "Maybe"]

        await ctx.send(random.choice(outputs))
        
    
    @commands.command(name='stop')
    async def stop(self, ctx):
        await self.bot.close()