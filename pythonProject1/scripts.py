import requests
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.implicitly_wait(50)
def moskv(partnumber):
    url = "http://portal.moskvorechie.ru/portal.api?p=ktp3M3tVkckOa5bgFB8IhMfnS93wOzBRbMZz3zypYuiHPIWgtLFcVA7zVCuxEzq0&act=price_by_nr_firm&v=1&cs=utf8&oe=1&extstor=1&alt=1&nr="+partnumber+"&l=arssenalavto"
    text_output = ''

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = json.loads(response.text)['result']
    for i in range(0,len(result)):
        if result[i]['stock'] != '0' and (result[i]['sname'] == 'Калуга'):
            text_output += '\n' + result[i]['brand'] + '\n' + result[i]['nr']  + '\nцена:' + result[i]['price'] + \
                       result[i]['currency'] + '\n' +  'на складе:' + result[i][
                           'stock'] + '\n'
        else:
            text_output += ''
    if text_output == '':
        return 'На данный момент, на Москворечье нет ничего подходящего в наличии'
    else:
        return 'Вот что есть на портале Москворечье:' + '\n' + '\n' + text_output

def rossko(partnumber):
    driver.get('https://klg.rossko.ru/')
    driver.implicitly_wait(10)
    log = driver.find_element(By.XPATH, "/html/body/div[1]/header/div[2]/div/div/nav/ul/li[2]/div/div/form/div[1]/input")
    passw = driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div/nav/ul/li[2]/div/div/form/div[2]/input')
    ActionChains(driver)\
        .move_to_element(log)\
        .click()\
        .send_keys('dastersilik@gmail.com')
    ActionChains(driver)\
        .move_to_element(passw)\
        .click()\
        .send_keys('123456')
    driver.find_element(By.XPATH,'/html/body/div[1]/header/div[2]/div/div/nav/ul/li[2]/div/div/form/div[4]/button').click()
