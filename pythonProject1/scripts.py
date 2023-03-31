from main import *
import requests
import json
def moskv(partnumber):
    url = "http://portal.moskvorechie.ru/portal.api?l=arssenalavto&p=7JSdPzITil0bDYbxv2jShC7oHjEfPjgmxpQ9IIUICNL0r5CuNOUEnbiT53kz4QWz&act=price_by_nr_firm&v=1&nr=" + partnumber + "&cs=utf8&oe=1&extstor=1&alt=1"
    text_output = ''

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = json.loads(response.text)['result']
    for i in range(0, len(result)//3):
        text_output += '\n' + result[i]['brand'] + '\n' + result[i]['name'] + '\n цена:' + result[i]['price'] + \
                       result[i]['currency'] + '\n последнее обновление: ' + result[i][
                           'upd'] + '\n мин. кол-во для заказа: ' + result[i]['minq'] + ', ' + 'на складе:' + result[i][
                           'stock'] + '\n'
    return 'Вот что есть на портале Москворечье:' + '\n' + '\n' + text_output



def rosko(partnumber):

    return 'Вот что есть на портале Роско:' + '\n' + '\n' + text_output