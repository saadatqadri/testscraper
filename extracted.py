from bs4 import BeautifulSoup
import urllib2
import re
import csv
from lxml import html
'''
soup = BeautifulSoup(open("eterracontrol_edited.htm"))
extracted = soup.find_all(style=re.compile("background:fuchsia"))

ofile = open('extract.htm', "w")

for line in extracted:
	print line
	cleaned_line = line.text.replace('\r\n', ' ').encode('utf-8')

	if (cleaned_line.isdigit() == False):
		ofile.write(cleaned_line)
		ofile.write('\n')

ofile.close()
'''

ofile = open('extract.txt', "rb")
#ofile2 = open('hl2_final.txt', 'w')
#ofile3 = open('hl3_final.txt', 'w')
#ofile4 = open('hl4_final.txt', 'w')
ofile5 = open('hl5_final.txt', 'w')


blob = ofile.readlines()

for line in blob:
	hl1_test = re.search(r'\d+\.\d+\.\d+', line)
	if hl1_test:
		
		if line.count('.') == 5:
			print line
			ofile5.write(line)
			ofile5.write('\n')

#ofile.close()
#ofile2.close()
#ofile3.close()
ofile5.close()