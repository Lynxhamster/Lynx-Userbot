from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.senggol(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GOBLOK GRUP SAMPAH ISI NYA PARA JAMET, NAJIS CUIHH*")
# Slipkol


@register(outgoing=True, pattern="^.aliangsi(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("*ALIANSI ALIANSI KTL BARU MAEN TELE SOK JADI PETINGGI, PINDAH FACEBOOK AJA ANJG LU GA COCOK MAEN TELE MUKA LU CEM KONTL INGET YA ALIANSI LU ITU SAMPAH GA LEBIH DARI MUNTAHAN BOCAH*")
# Menjawab Salam


@register(outgoing=True, pattern="^.gamon(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`GAMON EUY, GOYANGAN DIA BIKIN NAGIH🥺`")
# Istigfar


@register(outgoing=True, pattern="^.slipcrot(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"*BERAWAL*")
    sleep(2)
    await event.edit(f"*DARI SLIPKOL*")
    sleep(2)
    await event.edit("*BERUJUNG SLIPCROT*")
    sleep(2)
    await event.edit("*SLIPKOL = SLIPCROT !!*")
# Perkenalan


@register(outgoing=True, pattern="^.babu(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"*HALO BABU KU SEMUA APA KABAR?*")
    sleep(2)
    await event.edit(f"*MUDAH-MUDAH SEHAT YA 😎*")
    sleep(2)
    await event.edit("*KALO GAPUNYA DUIT MINTA KE GUA AJA*")
    sleep(2)
    await event.edit("*GUA KAN MAJIKAN LO !!*")

CMD_HELP.update({
    "Gabut aja": "**Modules** - `DI PAKE YA!!`\
    \n\n Cmd : `.senggol`\
    \nUsage : SENGGOL 1 GRUP\
    \n\n Cmd : `.aliangsi`\
    \nUsage : ROASTING ALIANSI TAI\
    \n\n Cmd : `.slipcrot`\
    \nUsage : CEK AJA SENDIRI
    \n\n Cmd : `.babu`\
    \nUsage : ROAST BABU
})
