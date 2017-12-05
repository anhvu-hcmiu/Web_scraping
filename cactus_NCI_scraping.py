from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep

import pandas as pd
import sys

vietherb_metabolite = pd.read_csv('/home/anhvu/vu_data/thesis/raw_benchmark/Vietherb_metabolite_plant.csv',sep='\t')
new_df = pd.DataFrame()
new_df['cas_id'] = vietherb_metabolite['metabolite']
new_df['plant'] = vietherb_metabolite['plant']

output = []

for cas_id in vietherb_metabolite['metabolite']:
    link = "https://cactus.nci.nih.gov/chemical/structure/" + str(cas_id) + "/smiles"
    
    try:     
        html_source = BeautifulSoup(urlopen(link).read(), "html.parser")
        smile = str(html_source.get_text())
        output.append(smile)
        print('{} is {}'.format(cas_id,smile))
              
    except:
        output.append('Unknown')
        print("Unknown")

new_df['SMILES'] = output
new_df.to_csv('/home/anhvu/vu_data/thesis/raw_benchmark/vietherb_smiles.csv', index=False)

print(Done)
