from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio


api = ""# API key
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())#переменная диспетчера

@dp.message_handler(commands = ["start"])#отрабатывает команду start
async def start_message(message):
    await message.answer("Привет! Я бот, помогающий твоему здоровью")#вывод сообщения в ТГбот

@dp.message_handler()#обрабатывает все входяшие сообщения,кроме команд
async def all_message(message):
    await message.answer("Введите команду /start, чтобы начать общение")#вывод сообщения в ТГбот

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)#переменная executor, запускающая диспетчер.