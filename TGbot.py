import logging
import wikipedia

from aiogram import Bot, Dispatcher, executor, types
wikipedia.set_lang('uz')

API_TOKEN = '5225699991:AAEf_Zws6DbIOeiiCWOO7UFy4nPHjqA2SEw'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):


    await message.reply("Hi!\nWelcome to Wikibot!")
    await message.reply("Bu Bot Siz Kiritgan So'zga Doir Malumotlarni Wikipediadan Topib Beradi.")


@dp.message_handler()
async def sendwiki(message: types.Message):
    try:
        respond = wikipedia.summary(message.text)
        await message.answer(respond)
    except:
        await message.answer("Bu Mavzuga Doir Malumot Topilmadi!")



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)