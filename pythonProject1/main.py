from scripts import *
import aiogram


global text_output
global partnumber

API_TOKEN = '6169576984:AAHm5TXIALWv-LPbcQq8X2wrgvpzmLHtYN4'

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: aiogram.types.Message):
    await message.reply('Привет! \nНапиши Артикул запчасти, и я найду на него самую выгодную цену!')


@dp.message_handler(content_types=['text'])
async def answ(message: aiogram.types.Message):
    partnumber = message.text
    await message.answer(moskv(partnumber))

    # url = 'http://klg.rossko.ru/service/v1/GetSearch?wsdl=&KEY1=dfbaadd0afa1523134d8bf00ce44f24c&KEY2=62b9f44a36189d9e23fe430bc53f7c68&text=' + partnumber
    # text_output = ''
    #
    # payload = {}
    # headers = {}
    #
    # response = requests.request("GET", url, headers=headers, data=payload)
    #
    # result = json.loads(response.text)
    # print(result)


if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)


