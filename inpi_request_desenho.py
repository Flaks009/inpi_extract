import requests
from bs4 import BeautifulSoup


headers = {
    'Host': 'gru.inpi.gov.br',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://gru.inpi.gov.br/pePI/jsp/desenhos/DesenhoSearchBasico.jsp',
    'Content-Type': 'application/x-www-form-urlencoded',
    'Content-Length': '173',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
    'cookie':'JSESSIONID=228031808983A33AC687CB7C58E23E7D.tecoa;'
    }

cookies = {
                'JSESSIONID':'228031808983A33AC687CB7C58E23E7D.tecoa',

            }

def cookie(url='https://gru.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp', headers=headers, cookies=cookies):
        jsession = requests.get(url, verify=False).headers['Set-Cookie'].split(';')
        cookies['JSESSIONID'] = jsession[0][11:]
        headers['Cookie'] += jsession[0]

def busca_pedido(cod, headers=headers, cookies=cookies):
    url = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController'



    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    with requests.Session() as s:
        x = s.post(url, headers=headers, cookies=cookies, data = payload, verify=False)

    return x



def busca_(cod, headers=headers, cookies=cookies):
    url = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController?Action=detail&CodPedido={}'.format(cod)

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    with requests.Session() as s:
        x = s.post(url, headers=headers, cookies=cookies, data = payload, verify=False)

    return x


def nome_procurador(soup):
    try:
        soup = BeautifulSoup(soup.text, 'html.parser')
        table = soup.find_all('table')
        table = table[1]
        tr = table.find_all('tr')

        for x in range(len(tr)):
            td = tr[x].find_all('td')
            for y in range(len(td)):
                try:
                    if '(74)' in td[y].find(class_='alerta').get_text():
                        print(td[y+1].find(class_ = 'normal').get_text())
                        return str(td[y+1].find(class_ = 'normal').get_text())
                except:
                    pass 
    except:
        pass

def cod_pedido(soup):
    try:
        soup = BeautifulSoup(soup.text, 'html.parser')
        for x in soup.find_all('a'):
            if 'CodPedido' in x.get('href'):
                o = (x.get('href'))
        try:
            o = o[53:75]
            res = [i for i in o if i.isdigit()]
            o = ''.join(res)
            return o
        except:
            pass
    except:
        pass