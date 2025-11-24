from aiogram import (Bot, Dispatcher, types)
from asyncio import run

from aiogram.filters import CommandStart

from config import BOT_TOKEN

bot = Bot(token=BOT_TOKEN)
dispatcher = Dispatcher()

async def main():
    await dispatcher.start_polling(bot)

@dispatcher.message(CommandStart())
async def hello_world(message: types.Message):
    await message.answer('Hello World!')

if __name__ == '__main__':
    run(main())