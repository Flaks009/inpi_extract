import requests
from bs4 import BeautifulSoup

def busca_pedido(cod):
    url = 'https://gru.inpi.gov.br/pePI/servlet/PatenteServletController'

    headers = {
        'Host': 'gru.inpi.gov.br',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://gru.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '173',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'cookie':'JSESSIONID=24FCE5A563DD92BA4061A8CCFACFE14D.tecod; _ga=GA1.3.1409685556.1587134600; _gid=GA1.3.1540987855.1587134600; _gat=1'
        }
    cookies = {'_ga':'GA1.3.1409685556.1587134600',
                'JSESSIONID':'24FCE5A563DD92BA4061A8CCFACFE14D.tecod',
                '_gid':'GA1.3.1540987855.1587134600',
                '_gat':'1'
                }

    payload = { 'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico',
                'NumPedido':cod
                }

    with requests.Session() as s:
        x = s.post(url, headers=headers, cookies=cookies, data = payload, verify=False)

    return x



def busca_(cod):
    url = 'https://gru.inpi.gov.br/pePI/servlet/PatenteServletController?Action=detail&CodPedido={}'.format(cod)

    headers = {
        'Host': 'gru.inpi.gov.br',
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
        'Accept-Language': 'pt-BR,pt;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Referer': 'https://gru.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': '173',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1',
        'cookie':'JSESSIONID=24FCE5A563DD92BA4061A8CCFACFE14D.tecod; _ga=GA1.3.1409685556.1587134600; _gid=GA1.3.1540987855.1587134600; _gat=1'
        }
    cookies = {'_ga':'GA1.3.1409685556.1587134600',
                'JSESSIONID':'24FCE5A563DD92BA4061A8CCFACFE14D.tecod',
                '_gid':'GA1.3.1540987855.1587134600',
                '_gat':'1'
                }

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