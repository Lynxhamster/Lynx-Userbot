from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern="^.slipkol(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`GUA NYARI SLIPKOLAN NIH, KALO LU SEDIH GABUT BISA KE GUA`")
# Slipkol


@register(outgoing=True, pattern="^.ange(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("`AYANG AKU ANGE 🥵 PENGEN PRIPET SM KM`")
# Menjawab Salam


@register(outgoing=True, pattern="^.gamon(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit("`GAMON EUY, GOYANGAN DIA BIKIN NAGIH🥺`")
# Istigfar


@register(outgoing=True, pattern="^.virtual(?: |$)(.*)")
async def perkenalan(event):
    event.pattern_match.group(1)
    await event.edit(f"`TMO TMO MULU`")
    sleep(2)
    await event.edit(f"`EMANG DAPET SLIPKOLAN?`")
    sleep(2)
    await event.edit("`MAKANYA GANTENG SAMA BERDUIT`")
    sleep(2)
    await event.edit("`MODAL CHATAN MANA BISA TOLOL`")
# Perkenalan


CMD_HELP.update({
    "Gabut aja": "**Modules** - `DI PAKE YA!!`\
    \n\n Cmd : `.slipkol`\
    \nUsage : POKOKNYA KEREN\
    \n\n Cmd : `.gamon`\
    \nUsage : CEK AJA DAH\
    \n\n Cmd : `.virtual`\
    \nUsage : UNTUK KOAR2 DI TMO"
})
