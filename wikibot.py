import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6402992099:AAG4frMt_ECMvGuev9_qz2Ik1AmFripAZbk'
wikipedia.set_lang('uz')
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)



@dp.message_handler(commands=["start", "help"])
async def welcome_bot(message: types.Message):
    await message.reply("Assalom alaykum.\nBotimizga xush kelibsiz!")


@dp.message_handler()
async def getwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu mavzuga oid ma'lumot topilmadi")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)