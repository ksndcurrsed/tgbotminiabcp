from scripts import *
import aiogram
from aiogram.dispatcher.filters import Text
from bs4 import BeautifulSoup
import pandas as pd

global text_output
global partnumber

API_TOKEN = '6169576984:AAHm5TXIALWv-LPbcQq8X2wrgvpzmLHtYN4'

bot = aiogram.Bot(token=API_TOKEN)
dp = aiogram.Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def welcome(message: aiogram.types.Message):
    await message.reply('Привет! \nНапиши Артикул запчасти, и я найду на него самую выгодную цену!')


@dp.message_handler(content_types=['text'])
async def answ(message: aiogram.types.Message, soup = BeautifulSoup):
    partnumber = message.text
    # await message.answer(moskv(partnumber))
    # await message.answer(rossko(partnumber))
    driver.get('https://klg.rossko.ru/auth')
    driver.find_element(By.XPATH, '//*[@id="auth_email"]').send_keys('dastersilik@gmail.com')
    driver.find_element(By.XPATH, '//*[@id="auth_password"]').send_keys('123456')
    driver.find_element(By.XPATH, '//*[@id="skin-layout"]/div/div/form/div[3]/div/button').click()
    driver.refresh()
    driver.find_element(By.XPATH, '//*[@id="1"]').send_keys(partnumber)
    driver.find_element(By.XPATH, '/html/body/div[1]/header/div[4]/div/div/div[2]/div/form/button').click()
    driver.find_element(By.XPATH, '//*[@id="skin-layout"]/div/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div[2]/div/div/a').click()
    elements1 = BeautifulSoup.soup.find_all(attrs={"class": {"src-features-product-card-components-variant-___index__col___fROoW src-features-product-card-components-variant-___index__brand___7OkgV"}})
    elements2 = BeautifulSoup.find_all(attrs={"class": {"src-features-product-card-components-variant-___index__link___AuZWk", "src-features-product-card-components-variant-___index__link___AuZWk"}})
    elements3 = BeautifulSoup.find_all(attrs={"class": {"src-bundyComponents-components-tooltip-___index__wrap___R0ORk src-features-product-card-components-stock-___deliver__tooltip___40YBm"}})
    elements4 = BeautifulSoup.find_all(attrs={"class": {"src-features-product-card-components-stock-___index__countContainer___j799B"}})
    elements5 = BeautifulSoup.find_all(attrs={"class": {"src-components-ProductPriceWithOverprice-___style__priceValue___iolAz"}})
    df = pd.DataFrame({'Производитель': [], 'номер': [], 'Наименование': [], 'Склад': [], 'Цена': []})
    for j in range(len(elements1)):
        df = df.append(
            {'Производитель': elements1[j].text, 'номер': elements2[j].text, 'Наименование': elements3[j].text,
             'Склад': elements4[j].text, 'Цена': elements5[j].text}, ignore_index=True)
    await message.answer(df)
if __name__ == '__main__':
    aiogram.executor.start_polling(dp, skip_updates=True)


