from scripts import *
import aiogram
from aiogram.dispatcher.filters import Text
from bs4 import BeautifulSoup
import pandas as pd
import lxml
import time

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
    # await message.answer(moskv(partnumber))
    # await message.answer(rossko(partnumber))
    driver.get('https://klg.rossko.ru/auth')
    driver.find_element(By.XPATH, '//*[@id="auth_email"]').send_keys('dastersilik@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="auth_password"]').send_keys('123456')
    driver.find_element(By.XPATH, '//*[@id="skin-layout"]/div/div/form/div[3]/div/button').click()
    driver.refresh()
    time.sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="1"]').send_keys(partnumber)
    time.sleep(3)
    driver.find_element(By.XPATH, '/html/body/div[1]/header/div[4]/div/div/div[2]/div/form/button').click()
    time.sleep(5)
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'lxml')
    vendor = soup.find('div', class_='wrapper').find('div', class_='skin layout').find('div', id_='main-group').find('section', class_='src-features-product-card-components-variant-___index__wrap___uvCfG src-features-product-card-components-variant-___index__open___F-w5c')
    print(vendor)
    #for quote in vendor:
       # print(quote.text)
if __name__ == '__main__':
    aiogram.executor.start_polling(dp)


