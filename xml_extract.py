import xml.etree.ElementTree as ET
import pandas as pd


def get_marca(nome_revista):
    tree = ET.parse('/home/ubuntu/inpi_extract/revistas/'+nome_revista+'.xml')
    root = tree.getroot()

    list_proc = []
    dict_attrib = {}

    for a in root.iter():
        if a.tag == 'processo':
            dict_attrib = {}
            dict_attrib.update(a.attrib)
            for b in a.iter():
                dict_attrib.update(b.attrib)
                if b.tag == 'procurador':
                    dict_attrib.update({b.tag : b.text})
            dict_attrib.update({'numero_rpi':nome_revista[2:]})
            list_proc.append(dict_attrib)
    
    df = pd.DataFrame(list_proc)

    df.to_excel('/home/ubuntu/inpi_extract/xlsx/{}.xlsx'.format(nome_revista[:5]))
    df.to_csv('/home/ubuntu/inpi_extract/xlsx/{}.csv'.format(nome_revista[:5]), index=False, sep=';')
