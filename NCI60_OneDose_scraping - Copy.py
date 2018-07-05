from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep

import pandas as pd
import sys

NSC_list = pd.read_csv('/home/anhvu/vu_data/thesis/raw_benchmark/filtered_OneDose_2016.csv') #blablablabla

smiles_list = open('/home/anhvu/vu_data/thesis/raw_benchmark/OneDose_SMILES.csv','w')

for i in NSC_list['NSC']:
    Done = False
    
    while not Done:
        try:
            link = 'https://dtp.cancer.gov/dtpstandard/servlet/Smiles?testshortname=SMILES&searchtype=NSC&searchlist=' + str(i)
            html_source = BeautifulSoup(urlopen(link).read(), "html.parser")
            td_tag = html_source.findAll("td")

            if len(td_tag) > 0:
                smiles = td_tag[2].get_text().strip()
                smiles_list.write(str(i))
                smiles_list.write('\t')
                smiles_list.write(smiles)
                smiles_list.write('\n')
                print("NSC {} is {}".format(i,smiles))
                Done = True
            else:
                smiles_list.write(str(i))
                smiles_list.write('\t')
                smiles_list.write('Unknown')
                smiles_list.write('\n')
                Done = True

        except:
            print("Internet connection error at NSC {}".format(i))
            sleep(5)
            pass

print("Done")