import discord
from discord.ext import commands
import aiohttp

def setup(bot):
    bot.add_cog(pokemon(bot))

class pokemon(commands.Cog): 
    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(name='pokemon')
    async def grab_pokemon(self, ctx, pokemon):
        poke_string = 'https://pokeapi.co/api/v2/pokemon/' +pokemon.lower()

        async with aiohttp.ClientSession() as session:
            async with session.get(poke_string) as response:
                req = await response.json()
                sprite = req['sprites']['other']['official-artwork']['front_default']

                embed = discord.Embed(title=pokemon)
                embed.set_thumbnail(url=sprite)

                await ctx.send(embed=embed)
                print(req)