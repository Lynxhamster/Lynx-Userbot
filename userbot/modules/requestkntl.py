from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.din(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**HAI... PERKENALKAN NAMAKU DINO, AKU DARI MANA MANA, UNCH DEH 🤪**")


@register(outgoing=True, pattern='^.noo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KATA DINOO KAMU TUH CACIMO BANGET SIH...**")


@register(outgoing=True, pattern='^.dno(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TAU GA SIH?? KALO DINO TUH LUCU BANGET 🤪**")
    
    
@register(outgoing=True, pattern='^.ccn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TITISAN DAJJAL GANTENG BAT 😎**")
    
    
@register(outgoing=True, pattern='^.ccn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CUMA KOMO YANG PALING GANTENG... 😎**")
    
    
@register(outgoing=True, pattern='^.odn(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DINOOO... AKU PADAMU...🥺**")


    
CMD_HELP.update({
    "requestan":
    ".din\
\nUsage: Punya Dino.\
\n\n.noo\
\nUsage: Punya Dino.\
\n\n.dno\
\nUsage: Punya Dino.\
\n\n.ccn\
\nUsage: Punya Cena.\
\n\n.moo\
\nUsage: Punya Komo.\
\n\n.odn\
\nUsage: Punya Dino."
})
