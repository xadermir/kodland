import discord
from discord.ext import commands

# Bot prefix ve intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Atıkların kategorileri
recycling_bins = {
    "plastik": ["pet şişe", "naylon", "plastik kap", "pipet"],
    "cam": ["cam şişe", "bardak", "kavanoz"],
    "metal": ["konserve", "teneke", "alüminyum kutu"],
    "kağıt": ["kitap", "defter", "gazete", "karton"],
    "organik": ["yemek artığı", "meyve kabuğu", "sebze kabuğu"],
    "elektronik": ["telefon", "pil", "batarya", "kulaklık"]
}

@bot.event
async def on_ready():
    print(f"{bot.user} olarak giriş yapıldı!")

@bot.command()
async def atik(ctx, *, atik_adi: str):
    atik_adi = atik_adi.lower()
    found = False
    
    for kategori, atiklar in recycling_bins.items():
        if atik_adi in atiklar:
            await ctx.send(f"🗑️ `{atik_adi}` -> **{kategori.upper()} kutusuna** atmalısın.")
            found = True
            break
    
    if not found:
        await ctx.send("🤔 Bu atığın hangi kutuya atılacağını bilmiyorum. Daha fazla bilgi için !yardim yazabilirsin.")

@bot.command()
async def yardim(ctx):
    mesaj = "♻️ **Atık Ayırma Rehberi**\n\n"
    for kategori, atiklar in recycling_bins.items():
        mesaj += f"**{kategori.upper()}**: {', '.join(atiklar)}\n"
    await ctx.send(mesaj)

# Bot tokenini buraya koy
bot.run("token")
