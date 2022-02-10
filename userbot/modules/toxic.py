from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.d(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PALALU GEDE KONTOL!! MAU GUA ENTOT LO PADA??**")


@register(outgoing=True, pattern='^.e(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAK USAH SOK KERAS GOBLOK!!KONTOL SEGEDE KELINGKING AJA BANYAK GAYA**")


@register(outgoing=True, pattern='^.f(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MUKA LU SEMUA KAYA KONTOL HAHAHAHA!!**")


@register(outgoing=True, pattern='^.i(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEMEK SEMPIT AJA BANGGA LU LONTHE!!**")


@register(outgoing=True, pattern='^.r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DIMANA ADA GIPEWE, DI SITU ADA GUA!!**")


@register(outgoing=True, pattern='^.t(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JINGKONTOT!!! ANJING!!BABI!!KONTOL!!NGENTOT!!!**")


@register(outgoing=True, pattern='^.u(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PALALO GEDE KONTOL!!GANTENGAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^.w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**LONTHE LU GOBLOK!!CANTIKAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^.z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**UDAH?? GITU DOANG?? BACOTAN LU GAK BIKIN GUA TREMOR GOBLOK HAHAHAHA!!**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ALLO ANJENGGG, PERKENALKAN NAMA SAYA ASSALAMUALAIKUM!!**")


@register(outgoing=True, pattern='^.n(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIMANA KABAR KAMU SAYANG??APAKAH BAIK?SEMOGA BESOK MATI YA...**")


@register(outgoing=True, pattern='^.b(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CUIHHH...MUKA DULU TUH BENERIN NGENTOT!!**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GRUB APA INI ANJENG!!, KOK SEPI BAT KEK HATI:)**")


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA DENGERIN GOBLOKKKK!!**")


@register(outgoing=True, pattern='^.s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSAH SOKAP DEH ANAK HARAM!!**")


@register(outgoing=True, pattern='^.v(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KEREN LU BEGITU NYET?? KEK SAMPAH YANG ADA**")


@register(outgoing=True, pattern='^.j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ANJENG NGERI BANYAK JAGOAN HAHAHAHA!!**")


@register(outgoing=True, pattern='^.a(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ALLAHUMMA AMIIN BISMILLAH SLEEP CALL!!😁**")


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**APAANSII SO KENAL BAT LU NGENTOT**")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SAYANGNYA AKU KEMANA YA??? AKU KANGENN...🥺**")


@register(outgoing=True, pattern='^.h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CANTIK LU BEGITU??? YANG ADA KEK LONTHE GOBLOK**")


@register(outgoing=True, pattern='^.o(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIKES AJA TERUS ANJENG AMPE LIMIT!!! MENANG GIPEWE NYA KAGAK PERNAH!! HAHHAHA**")


@register(outgoing=True, pattern='^.x(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MANA SOALNYA ANJENG!!! TURUNIN DOANG SUSAH AMAT NGENTOT!!**")


CMD_HELP.update({
    "toxic":
    f"{cmd}d\
\nUsage: Bacotin Orang.\
\n\n{cmd}e\
\nUsage: Buat Orang Yang Sok Keras.\
\n\n{cmd}f\
\nUsage: Ngatain Orang Wkwkkw.\
\n\n{cmd}i\
\nUsage: Kontol Orang Ngatain.\
\n\n{cmd}r\
\nUsage: Pantun Anjing.\
\n\n{cmd}t\
\nUsage: Nyebutin Binatang.\
\n\n{cmd}u\
\nUsage: Biar Dikata Ganteng.\
\n\n{cmd}w\
\nUsage: Biar Dikata Cantik.\
\n\n{cmd}z\
\nUsage: Tremor Kan Lu.\
\n\n{cmd}k\
\nUsage: Memperkenalkan Diri.\
\n\n{cmd}n\
\nUsage: Menanyakan Kabar.\
\n\n{cmd}b\
\nUsage: Sok Kepinteran.\
\n\n{cmd}m\
\nUsage: Gc Nya Kaya kuburan.\
\n\\{cmd}c\
\nUsage: Dia tuh Ngeyel banget.\
\n\n{cmd}s\
\nUsage: Haha sokap.\
\n\n{cmd}v\
\nUsage: Merendah.\
\n\n{cmd}a\
\nUsage: Nyari Sleep Call.\
\n\n{cmd}j\
\nUsage: Hujat yang gapunya muka.\
\n\n{cmd}g\
\nUsage: Kegantengan.\
\n\n{cmd}y\
\nUsage: teruntuk petarung.\
\n\n{cmd}h\
\nUsage: Kecantikan.\
\n\n{cmd}o\
\nUsage: Ngatain org norak.\
\n\n{cmd}x\
\nUsage: Ngatain Petarunx Tele."
})
