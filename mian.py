import asyncio
import logging
from aiogram import Bot, Dispatcher, F
from aiogram.filters.command import Command
from aiogram.types import Message, CallbackQuery
from buttons import keyboard, choises
from root import TOKEN

dp = Dispatcher()


@dp.message(Command("start"))
async def cmd_start(message: Message):
    await message.answer(
        f"Hello,{message.from_user.first_name} You can buy some household goods from me! My developer contact @bahromov_000",
        reply_markup=keyboard)


@dp.message(F.text == "🗂 Categories")
async def categories(message: Message):
    await message.answer("button choise", reply_markup=choises)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    bot = Bot(token=TOKEN)
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
