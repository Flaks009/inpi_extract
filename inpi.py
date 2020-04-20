from functools import reduce
import pandas as pd 
from main import main


def sum_list(a):
    x = {}
    for i in a:
        x = dict(x, **i)
    return [x]

a = open('P2565.txt', 'r')


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
df1 = df1.loc[df1['(Cd)'] == '(Cd) 15.21\n']
df1 = df1[:10]
df1['(21)'] = df1['(21)'].str.strip()
df1['(21)'] = df1['(21)'].str.slice(start=5)
df1_list = df1['(21)'].to_list()
l = []
for i in df1_list:
    l.append(main(i))
df1['procurador'] = l
df1 = df1[['(Cd)', '(71)', '(21)', 'procurador']]
df1.to_excel('test.xlsx')