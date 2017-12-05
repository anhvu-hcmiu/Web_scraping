from bs4 import BeautifulSoup
from urllib2 import urlopen
from time import sleep

def data_mining():
	f = open("/home/vuvu/vietherb_HMD/metabolite_plant.txt", "r").read().strip().split("\n")
	result = open("/home/vuvu/vietherb_HMD/HMD_result.csv", "w")
	number = 0
	for cas in f:
		Done = False
		while not Done:
			try:
				number += 1
				print str(cas), " #" + str(number)
				link = "http://www.hmdb.ca/unearth/q?utf8=%E2%9C%93&query=target&searcher=metabolites&button="
				url = link.replace("target", str(cas))
				html = urlopen(url).read()
				soup = BeautifulSoup(html, "html.parser")
				a = soup.findAll("tr")
				Description = []
				Synonyms =[]
				Formula = []
				Molecular = []
				IUPAC = []
				Traditional = []
				Super = []
				Class = []
				Sub = []
				Chebi = []
				for i in range(len(a)):
					try:
						if str(a[i].th.string) == "Description" and str(a[i+1].th.string) == "Kingdom":
						        pass
						elif str(a[i].th.string) == "Description" and str(a[i-1].th.string) == "Common Name":
							text = " ".join(a[i].td.get_text(strip=True).split()).encode("utf-8")
							Description.append(text) #DESCRIPTION APPEND
						elif str(a[i].th.string) == "Synonyms":
							for item in a[i].tbody("tr"):
								Synonyms.append(item.td.get_text().encode("utf-8")) #SYNONYMS APPEND
						elif str(a[i].th.string) == "Chemical Formula":
							Formula.append(a[i].td.get_text().encode("utf-8")) #CHEMICAL FORMULA APPEND
						elif str(a[i].th.string) == "Average Molecular Weight":		
							Molecular.append(a[i].td.get_text().encode("utf-8")) #MOLECULAR WEIGHT APPEND
						elif str(a[i].th.string) == "IUPAC Name":
							IUPAC.append(a[i].td.get_text().encode("utf-8")) #IUPAC APPEND
						elif str(a[i].th.string) == "Traditional Name":
							Traditional.append(a[i].td.get_text().encode("utf-8")) #TRADITIONAL NAME APPEND
						elif str(a[i].th.string) == "Super Class":
							Super.append(a[i].td.get_text().encode("utf-8")) #SUPER CLASS APPEND
						elif str(a[i].th.string) == "Class":
							Class.append(a[i].td.get_text().encode("utf-8")) #CLASS APPEND
						elif str(a[i].th.string) == "Sub Class":
							Sub.append(a[i].td.get_text().encode("utf-8")) #SUB CLASS APPEND
						elif str(a[i].th.string) == "ChEBI ID":
							Chebi.append(a[i].td.get_text().encode("utf-8"))  #CHEBI APPEND
					except:
						pass
				Description = ';'.join(Description)
				Synonyms = ';'.join(Synonyms)
				Formula = ';'.join(Formula)
				Molecular = ';'.join(Molecular)
				IUPAC = ';'.join(IUPAC)
				Traditional = ';'.join(Traditional)
				Super = ';'.join(Super)
				Class = ';'.join(Class)
				Sub = ';'.join(Sub)
				Chebi = ';'.join(Chebi)
				result.write(str(cas))
				result.write("\t")
				result.write(Description)
				result.write("\t")
				result.write(Synonyms)
				result.write("\t")
				result.write(Formula)
				result.write("\t")
				result.write(Molecular)
				result.write("\t")
				result.write(IUPAC)
				result.write("\t")
				result.write(Traditional)
				result.write("\t")
				result.write(Super)
				result.write("\t")
				result.write(Class)
				result.write("\t")
				result.write(Sub)
				result.write("\t")
				result.write(Chebi)
				result.write("\n")
				Done = True	
			except:
				sleep(0.5)
				pass
	result.close()
	print "DONE"

data_mining()

