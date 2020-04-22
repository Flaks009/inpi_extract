from functools import reduce
import pandas as pd 
from main import main_patente


def sum_list(a):
    x = {}
    for i in a:
        x = dict(x, **i)
    return [x]

nome_revista = input()
a = open(nome_revista, 'r')


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

df1 = df1.loc[(df1['(Cd)'] == '6.1')|(df1['(Cd)'] == '2.5')|(df1['(Cd)'] == '8.6')|(df1['(Cd)'] == '15.21')]

df1 = df1[df1['(71)'].str.contains('BR')]

df1['(21)'] = df1['(21)'].str.strip()
df1['(21)'] = df1['(21)'].str.slice(start=5)

df1['(21)'] = df1['(21)'].str.replace('A2','')
df1['(21)'] = df1['(21)'].str.replace('U2','')
df1['(21)'] = df1['(21)'].str.replace('A8','')

df1_list = df1['(21)'].to_list()
l = []
for i in df1_list:
    l.append(main_patente(i))
df1['Nome do Procurador'] = l
df1 = df1[['(Cd)', '(71)', '(21)', 'Nome do Procurador']]
df1[df1.columns] = df1.apply(lambda x: x.str.strip())
df1 = df1.rename(columns = {'(Cd)':'Código', '(71)':'Nome do Depositante', '(21)':'Número do Pedido'})
df1.to_excel('{}.xlsx'.format(nome_revista[4:]), index = False)