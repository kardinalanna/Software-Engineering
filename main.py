from config import TOKEN
from aiogram import Bot, types, utils
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from youtube_search import YoutubeSearch
import hashlib

def searcher(text):
    res = YoutubeSearch(text, max_results=10).to_dict()
    return res
    
bot = Bot(token=TOKEN)
dp = Dispatcher(bot)

@dp.inline_handler() #работа в inline режиме
executor.start_polling(dp, skip_updates=True)
