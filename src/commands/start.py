from mubble import Dispatch, Message, ParseMode
from mubble.rules import StartCommand

dp = Dispatch()


@dp.message(StartCommand())
async def start(message: Message):
    await message.answer(
        f"🔥 <b>{message.from_user.first_name}</b>, hiya!",
        parse_mode=ParseMode.HTML
    )
