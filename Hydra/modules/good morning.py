from Hydra import tbot as tbot
from Hydra.events import register

PHOTO = "https://te.legra.ph/file/7a18675abd9b75230735d.mp4"


@register(pattern=("Good morning"))
async def awake(event):
    NEKO = f" Welcome this beautiful morning with a smile on your face. I hope youll have a great day today. Wishing you a very good morning! {event.sender.first_name}"
    await tbot.send_file(event.chat_id, PHOTO, caption=NEKO)
