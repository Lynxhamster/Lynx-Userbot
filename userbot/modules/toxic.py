from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern='^.d(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BANGUSSS SETAN!!BAPA SIA ADUKEUN JEUNG BAGONG**")


@register(outgoing=True, pattern='^.e(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GOBLOK GOBLOK AJA ANJING, GAUSAH SOK PINTER NGENTOT!!**")


@register(outgoing=True, pattern='^.f(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**JINGKONTOT!!! ANJING!!KONTOL!!NGENTOT!!**")


@register(outgoing=True, pattern='^.i(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**DUA TIGA ANAK TOLOL, LO SEMUA KAYAK KONTOL!! HAHAHA**")


@register(outgoing=True, pattern='^.r(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**SYUTTT... TARIK NAFASS... HMM... BAU MEMEKK**")


@register(outgoing=True, pattern='^.t(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TETE TEPOS AJA BELAGU BAT LU LONTHE!!**")


@register(outgoing=True, pattern='^.u(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**PALALO GEDE KONTOL!!MASIH CAKEPAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^.w(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MEMEK LU BELATUNGAN!!MASIH CANTIKAN JUGA GUA HAHAHAHA**")


@register(outgoing=True, pattern='^.z(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**BACOT APASII???BACOTAN LU GAK BIKIN GUA TREMOR TOLOL HAHAHAHA!!**")


@register(outgoing=True, pattern='^.k(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**ALLO GAESS... WELCOLMEK PERKENALKAN NAMA SAYA ASSALAMU'ALAIKUM!!**")


@register(outgoing=True, pattern='^.n(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GIMANA KABAR KAMU SAYANG??APAKAH BAIK?SEMOGA BESOK MATI YA...**")


@register(outgoing=True, pattern='^.b(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**CUIHHH!!!HUEKKK!!! NAJISSS, MATI KEK LU NGENTOT!!**")


@register(outgoing=True, pattern='^.m(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GRUB GRUB APA YANG KAYAK KONTOL?? GRUB INI ANJING HAHAHA**")


@register(outgoing=True, pattern='^.c(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KAN UDAH GUA BILANG??MAKANYA DENGERIN GOBLOKKK!!**")


@register(outgoing=True, pattern='^.s(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**TOLOL BAT TOLOLL!! PASTI GA D SEKOLAHIN EMAKNYA!!**")


@register(outgoing=True, pattern='^.v(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KEREN LU BEGITU??**")


@register(outgoing=True, pattern='^.j(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**NGEURII BANYAK JAGOAN, LAWRIEEEEE HAHAHAHA!!**")


@register(outgoing=True, pattern='^.a(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**AYOK SLEEPCALL SAYANG🥺**")


@register(outgoing=True, pattern='^.g(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GWS ANAK HARAM!!**")


@register(outgoing=True, pattern='^.y(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**GAUSA SOK CANTIK LU NGENTOT!! MUKA KEK SEMPAK FIR'AUN AJA BELAGU BAT LONTHE!!**")


@register(outgoing=True, pattern='^.h(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**MAHAR PENGEN MILYARAN, NGULEK SAMBEL AJA KAGA BISA HAHAHAHA**")


@register(outgoing=True, pattern='^.o(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit("**KALO GA CANTIK MINIMAL GAUSAH SASIMO KAK🥴**")


CMD_HELP.update({
    "toxic":
    ".d\
\nUsage: Bacotin Orang.\
\n\n.e\
\nUsage: Buat Orang Yang Sok Keras.\
\n\n.f\
\nUsage: Ngatain Orang Wkwkkw.\
\n\n.i\
\nUsage: Kontol Orang Ngatain.\
\n\n.r\
\nUsage: Pantun Anjing.\
\n\n.t\
\nUsage: Nyebutin Binatang.\
\n\n.u\
\nUsage: Biar Dikata Ganteng.\
\n\n.w\
\nUsage: Biar Dikata Cantik.\
\n\n.z\
\nUsage: Tremor Kan Lu.\
\n\n.k\
\nUsage: Memperkenalkan Diri.\
\n\n.n\
\nUsage: Menanyakan Kabar.\
\n\n.b\
\nUsage: Sok Kepinteran.\
\n\n.m\
\nUsage: Gc Nya Kaya kuburan.\
\n\n.c\
\nUsage: Dia tuh Ngeyel banget.\
\n\n.s\
\nUsage: Haha sokap.\
\n\n.v\
\nUsage: Merendah.\
\n\n.a\
\nUsage: Nyari Sleep Call.\
\n\n.j\
\nUsage: Hujat yang gapunya muka.\
\n\n.g\
\nUsage: Kegantengan.\
\n\n.y\
\nUsage: teruntuk petarung.\
\n\n.h\
\nUsage: Kecantikan.\
\n\n.o\
\nUsage: Ngatain org norak."
})
