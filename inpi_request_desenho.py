import requests
from bs4 import BeautifulSoup
import urllib3
from requests.cookies import cookiejar_from_dict
import pickle
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def busca_pedido(cod):
    url_post = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController'

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    with open('params.pickle', 'rb') as p:
        params = pickle.load(p)
    
    s = requests.Session()
    x = s.post(url_post, headers=params['headers'], cookies = params['cookies'],data = payload, verify=False)

    return x




def busca_(cod):
    url_post = 'https://gru.inpi.gov.br/pePI/servlet/DesenhoServletController?Action=detail&CodPedido={}'.format(cod)

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    with open('params.pickle', 'rb') as p:
        params = pickle.load(p)
    
    s = requests.Session()
    x = s.post(url_post, headers=params['headers'], cookies = params['cookies'],data = payload, verify=False)

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