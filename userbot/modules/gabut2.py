from time import sleep
from userbot import CMD_HELP, DEVS
from userbot.events import register


@register(outgoing=True, pattern='^.Ouraaa(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Ouraaa`")
    sleep(3)
    await typew.edit("`90 Tahun`")
    sleep(3)
    await typew.edit("`JOMBLO`")
    sleep(1)
    await typew.edit("`Tinggal Di Mars, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Peka Ngapa Gblokkkk`")
    sleep(3)
    await typew.edit("`Akutuu Sayang Kamuu🥺`")
    sleep(1)
    await typew.edit("`I LOVE YOU SAYANG 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Menyerah`")
    sleep(1)
    await typew.edit("`Dan Selalu Tidurr`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.gelo(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("**HALLO ANAK ANAK ANJING....**")
    sleep(5)
    await typew.edit("**PERKENALKAN... KAMI SEKUMPULAN PARA BAJINGAN**")
    sleep(3)
    await typew.edit("**IZIN NIMBRUNG DI SINI...**")
    sleep(3)
    await typew.edit("**KAMI SEMUA INGIN MENGUCAPKAN...**")
    sleep(1)
    await typew.edit("**LO SEMUA KAYAK KONTOL!! YAHAHAHA WAHYU**")
# Create by myself @localheart


@register(outgoing=True, pattern='^.chif(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`CHIFUYU DATANG`")
    sleep(5)
    await typew.edit("`SLEBEWWW...`")
    sleep(3)
    await typew.edit("`SLEMEKKK...`")
    sleep(3)
    await typew.edit("`SKNTOLL...`")
    sleep(1)
    await typew.edit("`BAPA LU COSPLAY UBIII...`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.ouraaa`\
    \n↳ : perkenalan Bdrl\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
    \n↳ : Jan Lupa Semangat`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.gelo`\
    \n↳ : Orang Sinting`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.chif`\
    \n↳ : Welcome Chifuyu."
})
