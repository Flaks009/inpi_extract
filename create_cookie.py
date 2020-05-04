import requests
from bs4 import BeautifulSoup
import urllib3
from requests.cookies import cookiejar_from_dict
import pickle
import datetime
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
        dict_params = {}
        dict_params['headers'] = s.headers
        dict_params['cookies'] = s.cookies
        
        print(dict_params)

        with open('params.pickle', 'wb') as fp:
            pickle.dump(dict_params, fp)