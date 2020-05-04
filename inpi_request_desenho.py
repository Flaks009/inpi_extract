import requests
from bs4 import BeautifulSoup
import urllib3
from requests.cookies import cookiejar_from_dict
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


headers = {
'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
}


def create_cookie(headers = headers):
    url_get = 'https://gru.inpi.gov.br/pePI/servlet/LoginController?action=login'
    with requests.Session() as s:
        s.headers.update(headers)
        s.get(url_get, headers = headers, verify=False)
        cookieJar = s.cookies.get_dict()
        cookieJar = cookiejar_from_dict(cookieJar)
        s.headers.update({'Cookie':'JSESSIONID={};'.format(cookieJar['JSESSIONID'])})
        return s


def busca_pedido(cod,s,headers=headers):
    url_post = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController'

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    x = s.post(url_post, data = payload, verify=False)
    return x



def busca_(cod,s,headers=headers):
    url_post = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController?Action=detail&CodPedido={}'.format(cod)

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }


    x = s.post(url_post, data = payload, verify=False)

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