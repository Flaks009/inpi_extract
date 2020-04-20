import requests

url = 'https://gru.inpi.gov.br/pePI/jsp/patentes/PatenteSearchBasico.jsp'

with requests.Session() as s:
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
        'Upgrade-Insecure-Requests': '1'
        }
    payload = {'NumPedido':'BR+11+2020+003756-7',
               'FormaPesquisa':'todasPalavras',
                'botao':'+pesquisar+%BB+',
                'Action':'SearchBasico'}

    cookies = {'_ga':_'GA1.3.1409685556.1587134600', 'JSESSIONID':'AF4D8E1E981415EF2FAF61AB03709272.tecod', '_gid':'GA1.3.1540987855.1587134600',}

    x = s.post(url, data = payload, headers=headers, cookies=cookies, verify=False)



