import requests
from bs4 import BeautifulSoup
import urllib3
import json
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

rpi = requests.get('http://revistas.inpi.gov.br/rpi/')

soup = BeautifulSoup(rpi.text)

table = soup.findAll('table')[0].findAll('tr')

rpi_list = []
rpi_dict = {'Revistas': rpi_list}

for t in table:
    try:
        row = t.find('td')
        rpi_dict['Revistas'].append(row.text)
    except:
        print('Error')

with open('/home/ubuntu/flask_test_app/app/json_files/rpi.json', 'w') as fp:
    json.dump(rpi_dict, fp)