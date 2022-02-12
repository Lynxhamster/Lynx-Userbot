from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^P(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐒𝐀𝐋𝐀𝐌𝐔'𝐀𝐋𝐀𝐈𝐊𝐔𝐌, 𝐆𝐀 𝐉𝐀𝐖𝐀𝐁 𝐏𝐊𝐈!!!")


@register(outgoing=True, pattern='^.atg(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐀𝐒𝐓𝐀𝐆𝐇𝐅𝐈𝐑𝐔𝐋𝐋𝐀𝐇 𝐌𝐀𝐍𝐓𝐀𝐏😭")


@register(outgoing=True, pattern='^L(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐖𝐀'𝐀𝐋𝐀𝐈𝐊𝐔𝐌𝐒𝐀𝐋𝐀𝐌 𝐀𝐍𝐀𝐊 𝐒𝐄𝐓𝐀𝐍!!!")


@register(outgoing=True, pattern='^.ast(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("𝐘𝐔 𝐁𝐈𝐒𝐀 𝐘𝐔... 𝐀𝐒𝐘𝐇𝐀𝐃𝐔... 😭")


CMD_HELP.update({
    "salam":
    "P\
\nUsage: Untuk Memberi salam.\
\n\nL\
\nUsage: Untuk Menjawab Salam."
})


CMD_HELP.update({
    "salam2":
    ".atg\
\nUsage: Istighfar 1.\
\n\n.ast\
\nUsage: Istighfaf 2."
})
