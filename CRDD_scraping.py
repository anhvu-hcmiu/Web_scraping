
from bs4 import BeautifulSoup
from urllib.request import urlopen
from time import sleep
import sys

def data_scraping(compound_name):
    key_link = 'http://crdd.osdd.net/raghava/npact/search_cmpnd.php?cmpnd='
    key_link = key_link + compound_name
    html = urlopen(key_link).read() 
    soup = BeautifulSoup(html, "html.parser")
    td_tag = soup.findAll("td")
    
    result = []
    
    for index in range(0,len(td_tag)):
        if td_tag[index].get_text() == 'PubChem Id':
            result.append(td_tag[index+1].get_text())
        elif td_tag[index].get_text() == 'Class':
            result.append(td_tag[index+1].get_text())
        elif td_tag[index].get_text() == 'SMILES':
            result.append(td_tag[index+1].get_text())
    
    return result

def main(file_input,file_output):
    output = open(file_output, 'w')
    list_compounds = open(file_input).read().split('\n')

    for index, compound in enumerate(list_compounds):
        Done = False
        while not Done:
            try:
                retrieved_item = data_scraping(compound)
                if len(retrieved_item) > 0:
                    output.write(compound)
                    output.write('\t')            
                    output.write(retrieved_item[0])
                    output.write('\t')
                    output.write(retrieved_item[1])
                    output.write('\t')
                    output.write(retrieved_item[2])
                    output.write('\n')
                    print('Done ' + compound + ' ' + str(index))
                    Done = True
                else:
                    output.write(compound)
                    output.write('\n')
                    print(index)
                    Done = True
                    pass

            except:
                sleep(0.5)
                pass

main(*sys.argv[1:])
