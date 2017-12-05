### Import
from bs4 import BeautifulSoup
from urllib2 import urlopen

### List of Tree needed to attain data
def tree_list():
	directory = "/home/vuvu/vietherb_knapsack/vietherb_treelist.txt"
	f = open(directory, "r").read().strip().split("\n")
	f2 = []
	for i in f:
		f2.append(i.replace(" ", "%20")) #Add %20 for link
	return f2

### Scraping data for C_ID and CAS_ID
def knapsack_datamining():
	result = open("/home/vuvu/vietherb_knapsack/knapsack_result.csv", "w")
	plant = tree_list()
	n = 0
	for i in plant:
		n += 1 # List out the number of tree downloading
		link = "http://kanaya.naist.jp/knapsack_jsp/result.jsp?sname=all&word=" + i
		html = urlopen(link).read() 
		soup = BeautifulSoup(html, "html.parser")
		a = soup.findAll("tr")
		refine_plant = i.replace("%20", " ") #Give the name back to the original version
		c_id = []
		cas_id = []
		print refine_plant, str(n)
		for item in range(len(a)-1):
			x = str(a[item].findAll("td")[0].next.next.string) # Data for C_ID
			y = str(a[item].findAll("td")[1].next.string) # Data for  CAS_ID
			c_id.append(x)
			cas_id.append(y)
		result.write(refine_plant)
		result.write("\t")
		result.write(';'.join(c_id))
		result.write("\t")
		result.write(';'.join(cas_id))
		result.write("\n")
	result.close()

tree_list()
knapsack_datamining()
