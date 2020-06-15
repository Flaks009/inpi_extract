from functools import reduce
import pandas as pd 
import os
from main import main_patente, main_desenho
from create_cookie import create_cookie
from xml_extract import get_marca

create_cookie()

def sum_list(a):
    x = {}
    for i in a:
        x = dict(x, **i)
    return [x]

nome_revista = input('Numero da revista:')
os.system('/home/ubuntu/inpi_extract/download.sh {0} {1}'.format(nome_revista[:2], nome_revista[2:]))

nome_revista = nome_revista.upper()

if 'I' in nome_revista:
    nome_revista = nome_revista.replace('I', '')
elif 'RM' in nome_revista:
    a = open('/home/ubuntu/inpi_extract/revistas/'+nome_revista+'.xml', 'r', encoding='utf-8')
    get_marca(nome_revista)
    os.system('/home/ubuntu/inpi_extract/exclude.sh')
    exit() 

a = open('/home/ubuntu/inpi_extract/revistas/'+nome_revista+'.txt', 'r', encoding='utf-8')


list_cd = []
list_r = []


for i in a:
    if '(Cd)' in i:
        list_cd.append(list_r)
        list_r = []
    list_r.append({str(i[:4]):i})

test = []
for c in list_cd:
    for d in c:
        if d.keys() not in test:
            test.append(d.keys())

list_cd = list_cd[2:]
test = test[2:]

df = pd.DataFrame(columns = test)

df_lambda = lambda x: pd.DataFrame.from_dict(x)
df1 = map(lambda x: sum_list(x), list_cd)
df1 = map(df_lambda, df1)
df1 = reduce(lambda df, df_: pd.concat([df,df_], sort = False), df1)
df1[df1.columns] = df1.apply(lambda x: x.str.strip())
df1['(Cd)'] = df1['(Cd)'].apply(lambda x: x[4:])
df1[df1.columns] = df1.apply(lambda x: x.str.strip())

if nome_revista[0] == 'P':
    df1 = df1.loc[(df1['(Cd)'] == '6.1')|
    (df1['(Cd)'] == '2.5')|
    (df1['(Cd)'] == '8.6')|
    (df1['(Cd)'] == '15.21')|
    (df1['(Cd)'] == '121')|
    (df1['(Cd)'] == '205')|
    (df1['(Cd)'] == '1.5')|
    (df1['(Cd)'] == '6.1')|
    (df1['(Cd)'] == '6.7')|
    (df1['(Cd)'] == '6.21')|
    (df1['(Cd)'] == '6.22')|
    (df1['(Cd)'] == '7.1')|
    (df1['(Cd)'] == '9.2')|
    (df1['(Cd)'] == '11.1')|
    (df1['(Cd)'] == '11.2')
    ]
elif nome_revista[0] == 'D':
    df1 = df1.loc[(df1['(Cd)'] == '33.1')|
    (df1['(Cd)'] == '34')|
    (df1['(Cd)'] == '30')|
    (df1['(Cd)'] == '36')|
    (df1['(Cd)'] == '37')|
    (df1['(Cd)'] == '41')
    ]




df71 = df1[df1['(71)'].str.contains('BR', na=False)]
df73 = df1[df1['(73)'].str.contains('BR', na=False)]
df1 = pd.concat([df71, df73])
df1['(21)'] = df1['(21)'].combine_first(df1['(11)'])


df1['(21)'] = df1['(21)'].str.strip()
df1['(21)'] = df1['(21)'].str.slice(start=5)

df1['(21)'] = df1['(21)'].str.replace('A8|A2|B1|B8|C8|E2|E8|F1|F8|G8|U2|U8|Y1|Y8|Z8','')

df1_list = df1['(21)'].to_list()
l = []

if nome_revista[0] == 'D':
    for i in df1_list:
        l.append(main_desenho(i))
elif nome_revista[0] == 'P':
    for i in df1_list:
        l.append(main_patente(i))


df1['Nome do Procurador'] = l
df1 = df1[['(Cd)', '(71)', '(73)', '(21)', 'Nome do Procurador']]
df1[df1.columns] = df1.apply(lambda x: x.str.strip())
df1 = df1.rename(columns = {'(Cd)':'codigo', '(71)':'nome_do_depositante', '(73)':'nome_do_autor', '(21)':'numero_do_pedido'})
df1['numero_rpi'] = nome_revista[2:]
df1.to_excel('/home/ubuntu/inpi_extract/xlsx/{}.xlsx'.format(nome_revista[:6]), index = False)
df1.to_csv('/home/ubuntu/inpi_extract/xlsx/{}.csv'.format(nome_revista[:6]), index = False, sep=';')

os.system('/home/ubuntu/inpi_extract/exclude.sh')