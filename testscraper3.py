from bs4 import BeautifulSoup
import urllib2
import re
import csv
from lxml import html
import json


soup = BeautifulSoup(open("eterracontrol_subset.htm"))

# find the section
# find the first <h3> tag
section_header = soup.find('h3').span.text.replace("\n", '')

# find the first <h4> tag
func_area_header = soup.find('h4').span.text.replace('\n','')

# find the first <h5> tag
test_title = soup.find('h5').span.text.replace('\n','')
# find the next p tag

# find the description, strip the whitespace
test_description_tag = soup.find('h5').find_next_sibling("p")
test_description = test_description_tag.text.replace('\n', ' ')

# find the estimated time, if any
test_estimate_tag = test_description_tag.find_next("p")

test_

if (test_estimate_tag.text.find("Estimated") != -1):
	test_estimate = test_estimate_tag.text
	test_setup_tag = test_estimate_tag.find_next("p")
else:
	test_estimate = ""
	test_setup_tag = test_estimate_tag

test_setup = test_setup_tag.text 


test = {"section": section_header,
		"functional_area": func_area_header,
		"title": test_title,
		"description": test_description,
		"estimate": test_estimate,
		"setup": test_setup, 
}

print json.dumps(test)





















#hl = soup.find_all('span', attrs={'style':"mso-no-proof:yes"})

ofile = open('hl5.csv', "w")

for hl5 in soup.findAll('p', attrs={'class':"MsoToc5"}):
	test_with_dots = hl5.span.extract()
	
	try:
		dots = test_with_dots.span.extract()
		test_final = test_with_dots.string.replace('\r\n', ' ').encode('utf-8')

	except AttributeError:
		test_final = 'SKIPPED'
		pass

	print test_final
	ofile.write(test_final)
	ofile.write('\n')
	#print hl2.span.text


ofile.close()


'''

hl2 = soup.find_all('p', attrs={'class':"MsoToc2"})
ofile = open('hl2.csv', "w")

for header in hl2:
	print header.get_text()
	ofile.write(header.get_text())
	ofile.write('\n')

ofile.close()



hl3 = soup.find_all('p', attrs={'class':"MsoToc3"})
ofile = open('hl3.csv', "w")

for header in hl3:
	print header.get_text()
	ofile.write(header.get_text())
	ofile.write('\n')

ofile.close()



hl4 = soup.find_all('p', attrs={'class':"MsoToc4"})
ofile = open('hl4.csv', "w")

for header in hl4:
	print header.get_text()
	ofile.write(header.get_text().encode('utf-8'))
	ofile.write('\n')

ofile.close()



#test_title = soup.h2.a.next_sibling.get_text()
#print(test_title)
#test_desc = soup.p

#alltext = soup.get_text()

#print(alltext)



#print(soup.prettify())

#tag = soup.h2

#print tag.name

#header2 = soup.find_all('span', attrs= {'lang':'EN-US'}),

#print header2

#for eachh in header2:
#	print(type(eachh))
#	print(eachh.string)	
	#print(eachh.prettify())		
	#print(eachh.a.contents)


#url = "http://www.utexas.edu/world/univ/alpha"
#page = urllib2.urlopen(url)
#soup = BeautifulSoup(page.read())

#universities = soup.findAll('a', {'class':'institution'})

#for eachuniversity in universities:
#	print eachuniversity['href']+","+eachuniversity.string
	 '''
