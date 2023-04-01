import requests
import json
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
    url = 'http://klg.rossko.ru/service/v1/GetSearch?wsdl=&KEY1=dfbaadd0afa1523134d8bf00ce44f24c&KEY2=62b9f44a36189d9e23fe430bc53f7c68&text=' + partnumber
    text_output = ''

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    result = json.loads(response.text)
    print(result)

