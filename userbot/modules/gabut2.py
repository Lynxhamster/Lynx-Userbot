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
    await typew.edit("`Tinggal Di Jawa, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Menyerah`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.trio(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai saya trio kontolllll `")
    sleep(5)
    await typew.edit("`perkenalkan saya @aulri biasa di sebut anak haram, lanjut.`")
    sleep(3)
    await typew.edit("`saya @zenzuzu2 anak anj`")
    sleep(3)
    await typew.edit("`Dan saya @Ekojuuuuu pria idaman`")
    sleep(1)
    await typew.edit("`Kami bertiga tolol dan donggo 🥵`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `ouraaa`\
    \n↳ : perkenalan Bdrl\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
    \n↳ : Jan Lupa Semangat."
})
