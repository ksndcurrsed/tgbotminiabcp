import aiogram
import requests
import json
# from selenium import webdriver
# from selenium.webdriver.common.by import By
global text_output

API_TOKEN = '6169576984:AAHm5TXIALWv-LPbcQq8X2wrgvpzmLHtYN4'
#
# driver = webdriver.Firefox()

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)

partnumber = 0

moskusername = "arssenalavto"
moskpassword = "3O3COJFGu"

@dp.message_handler(commands=['start'])
async def welcome(message: aiogram.types.Message):
    await message.reply('Привет! \nНапиши Артикул запчасти, и я найду на него самую выгодную цену!')


@dp.message_handler(content_types=['text'])
async def echo(message: aiogram.types.Message):
    global partnumber, moskusername, moskpassword
    partnumber = message.text
    url = "http://portal.moskvorechie.ru/portal.api?l=arssenalavto&p=7JSdPzITil0bDYbxv2jShC7oHjEfPjgmxpQ9IIUICNL0r5CuNOUEnbiT53kz4QWz&act=price_by_nr_firm&v=1&nr="+partnumber+"&cs=utf8&oe=1&extstor=1&alt=1"
    text_output = ''

    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = json.loads(response.text)['result']
    for i in range(0,len(result)):
        text_output += '\n' + result[i]['brand'] + ' - ' + result[i]['name'] + '\n цена:' + result[i]['price'] + '\n'
        print(text_output)
    await message.answer(text_output)





if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)


