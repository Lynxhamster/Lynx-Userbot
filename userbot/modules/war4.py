# ReCode by @Kayyzyu
# FROM Kayzyu-Ubot <https://github.com/Kayzyu/Kayzu-Ubot>
# KONTOLLLLLLL

from platform import uname
from userbot import ALIVE_NAME, CMD_HELP
from userbot.events import register

# ================= CONSTANT =================
DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else uname().node
# ============================================


@register(outgoing=True, pattern=r"^\.roas(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**NAJIS  YE JADI ORANG JANGAN CUMA BEBAN KELUARGA, BEBAN NEGARA, BEBAN DUNIA AKHRAT TOLOL,YE KERJA DONGO,KAGA ADA YANG MAU JUGA MERHATIIN ORANG HINA KEK LU SADAR DIRI LU ANAK HARAM**")


@register(outgoing=True, pattern=r"^\.roas1(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GUA TAU KALO LU KAGA PUNYA DUIT BUAT BELI SKINCARE KAN TOLOL ORANG MISKIN KEK LU CUMA BISA MAKE TEPUNG TERIGU, DIKASIH AER BIAR AGAK PUTIHAN JATOHNYA KAGA NGEFEK TOLOL MUKA LU MALAH KEK DONAT BASI BEGO**")


@register(outgoing=True, pattern=r"^\.roas3(?: |$)(.*)")
async def typewriter(typew):
    typew.pattern_match.group(1)
    await typew.edit(
        "**GA USAH SO MANTEP BEGO KALO LEHER MASIH BEDAKI SELANGKANGAN BEJAMUR KONTOL NANAHAN MAKANYA KALO MANDI PAKE AIR BUKAN PAKE PASIRGUA JAGO GA KAYA LU YG SOSOAN JADI JAGOAN KOSA KATA CUMA SATU-10 TERUS DIBALIKIN SEPULUH-SATU,SAMA KAYA HIDUP LU MUNDAR MANDIR SANA SINI CARI PINJEMAN BUAT MAKAN SEHARI HARI YEKAN SAMPE KAPAN PUN GUA BAKALAN LADENIN LU GOBLOKLADENIN MANUSIA PURBA JELEK KEK LU GABAKALAN BERENTI GUA TOLOL**")


CMD_HELP.update(
    {
        "war3": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas1\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas2\
        \n↳ : lihat sendiri\
        \n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: .roas3\
        \n↳ : lihat sendiri\
        \n↳ **COBAIN AJA SENDIRI SEMUA!**.\
   "
    }
)
