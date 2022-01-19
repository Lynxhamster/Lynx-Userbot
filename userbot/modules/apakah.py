import random
from userbot.events import register

APAKAH_STRING = ["Iya", 
                 "Tidak", 
                 "Mungkin",
                 "Bisa jadi", 
                 "Mungkin Tidak",
                 "Tidak Mungkin",
                 "YNTKTS",
                 "Pala bapak kau pecah",
                 "Apa iya?",
                 "Tanya aja sama mamak kau tu lah"
                 "Mungkin iya",
                 "Mungkin",
                 "Iya",
                 "Tidak",
                 "Nggak tau",
                 "Benar",
                 "Aalah",
                 "Lu kali bukan dia",
                 "Apa iya",
                 "Kayaknya",
                 "Ah masa",
                 "Masa sih",
                 "Oh gitu ya",
                 "Oh oke",
                 "Stres",
                 "Apasih",
                 "Gak jelas",
                 "Keren",
                 "Tolol",
                 "Anjing",
                 "Anjir",
                 "Goblok",
                 "Ganteng",
                 "Jelek",
                 "Bapakau",
                 "Dadjal",
                 "Setan",
                 "Iblis",
                 ]


@register(pattern="^apakah ?(.*)")
async def apakah(event):
    quew = event.pattern_match.group(1)
    if not quew:
        await event.reply('Berikan saya pertanyaan kontol 😐')
        return
    await event.reply(random.choice(APAKAH_STRING))
