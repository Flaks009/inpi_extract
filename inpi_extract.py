from functools import reduce
import pandas as pd 
from main import main_patente, main_desenho
from create_cookie import create_cookie


def sum_list(a):
    x = {}
    for i in a:
        x = dict(x, **i)
    return [x]

nome_revista = input('Numero da revista:')
nome_revista = nome_revista.upper()
a = open(nome_revista+'.txt', 'r', encoding='utf-8')


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
    df1 = df1.loc[(df1['(Cd)'] == '6.1')|(df1['(Cd)'] == '2.5')|(df1['(Cd)'] == '8.6')|(df1['(Cd)'] == '15.21')]
elif nome_revista[0] == 'D':
    df1 = df1.loc[(df1['(Cd)'] == '33.1')|(df1['(Cd)'] == '34')]



df1 = df1[df1['(71)'].str.contains('BR')]

df1['(21)'] = df1['(21)'].str.strip()
df1['(21)'] = df1['(21)'].str.slice(start=5)

kind_codes = ['A2','A8','B1','B8','C8','E2','E8','F1','F8','G8','U2','U8','Y1','Y8','Z8']

df1['(21)'] = df1['(21)'].str.replace('U2','')
df1['(21)'] = df1['(21)'].str.replace('A8','')
df1['(21)'] = df1['(21)'].str.replace('A2','')
df1['(21)'] = df1['(21)'].str.replace('A8','')
df1['(21)'] = df1['(21)'].str.replace('B1','')
df1['(21)'] = df1['(21)'].str.replace('B8','')
df1['(21)'] = df1['(21)'].str.replace('C8','')
df1['(21)'] = df1['(21)'].str.replace('E2','')
df1['(21)'] = df1['(21)'].str.replace('E8','')
df1['(21)'] = df1['(21)'].str.replace('F1','')
df1['(21)'] = df1['(21)'].str.replace('F8','')
df1['(21)'] = df1['(21)'].str.replace('G8','')
df1['(21)'] = df1['(21)'].str.replace('U2','')
df1['(21)'] = df1['(21)'].str.replace('U8','')
df1['(21)'] = df1['(21)'].str.replace('Y1','')
df1['(21)'] = df1['(21)'].str.replace('Y8','')
df1['(21)'] = df1['(21)'].str.replace('Z8','')

df1_list = df1['(21)'].to_list()
l = []

if nome_revista[0] == 'D':
    for i in df1_list:
        l.append(main_desenho(i))
elif nome_revista[0] == 'P':
    for i in df1_list:
        l.append(main_patente(i))


df1['Nome do Procurador'] = l
df1 = df1[['(Cd)', '(71)', '(21)', 'Nome do Procurador']]
df1[df1.columns] = df1.apply(lambda x: x.str.strip())
df1 = df1.rename(columns = {'(Cd)':'Código', '(71)':'Nome do Depositante', '(21)':'Número do Pedido'})
df1.to_excel('{}.xlsx'.format(nome_revista[:5]), index = False)