import discord
import gsc
from discord import app_commands
from config import settings
import categories

intents = discord.Intents.default()
client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)

@client.event
async def on_ready():
    await tree.sync(guild = discord.Object(id = settings['id']))
    print(f"Logged in as {client.user} (ID: {client.user.id})")


@tree.command(name = "facsgo", description = "Shows faceit CS:GO stats", guild=discord.Object(id=731480774209175552)) 
async def ds_fcsgo(interaction, nick: str):
    await interaction.response.defer()

    try:
        stats = gsc.faceit_csgo(nick)
        embed = discord.Embed(
            title = "⠀",
            description = "Main stats",
            color = 0xFF5733
        )
        embed.set_author(name=f"{nick}'s stats", icon_url=stats[12])

        for i in range(6):
            embed.add_field(name = categories.fcsgo_category[i], value = stats[i], inline = True)
        
        embed.add_field(name = "⠀", value = "Last 10 matches average stats", inline = False)
       
        for i in range(6, 12):
            embed.add_field(name = categories.fcsgo_category[i], value = stats[i], inline = True)

        await interaction.followup.send(embed=embed)

    except:
        await client.get_channel(settings["channel"]).send("You bruh")


@tree.command(name = "osu", description = "Shows OSU! stats", guild=discord.Object(id=settings["id"])) 
async def ds_osu(interaction, nick: str):
    await interaction.response.defer()

    try:
        stats = gsc.osu(nick)
        embed = discord.Embed(
            title = "⠀",
            description = "Main stats",
            color = 0xAC396D
        )
        # embed.set_author(name=f"{nick}'s stats", icon_url=stats[15])

        for i in range(5):
            embed.add_field(name = categories.osu_category[i], value = stats[i], inline = True)
        
        embed.add_field(name = "⠀", value = "Marks", inline = False)
       
        for i in range(5, 10):
            embed.add_field(name = categories.osu_category[i], value = stats[i], inline = True)

        embed.add_field(name = "⠀", value = "Other stats", inline = False)
       
        for i in range(10, 15):
            embed.add_field(name = categories.osu_category[i], value = stats[i], inline = True)

        await interaction.followup.send(embed=embed)

    except:
        await client.get_channel(975565397598306354).send("You bruh")


@tree.command(name = "fort", description = "Shows this fortnite seasons stats", guild=discord.Object(id=731480774209175552)) 
async def ds_fort(interaction, nick: str):
    await interaction.response.defer()

    try:
        stats = gsc.fort(nick)
        embed = discord.Embed(
            title = "⠀",
            description = "This seasons stats",
            color = 0x4DABE7
        )
        embed.set_author(name=f"{nick}'s stats", icon_url="https://upload.wikimedia.org/wikipedia/commons/7/7c/Fortnite_F_lettermark_logo.png?20210818022222")

        for i in range(6):
            embed.add_field(name = categories.fort_category[i], value = stats[i], inline = True)
        
        await interaction.followup.send(embed=embed)

    except:
        await client.get_channel(settings['channel']).send("You bruh")

client.run(settings["token"])
# test
