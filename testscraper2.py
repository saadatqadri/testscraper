import os, json
import re

test = {}

f2 = open('hl2.csv', 'r')
f3 = open('hl3.csv', 'r')
f4 = open('hl4.csv', 'r')
f5 = open('hl5.csv', 'r')

hl2_list = f2.readlines()
for hl2 in hl2_list:
	hl2_num = re.search(r'\d+\.\d+', hl2)
	print hl2_num.group()
	test['hl2_num'] =hl2_num.group()

	hl2_title = re.findall(r'(\w+)', hl2)
	print ' '.join(hl2_title[2:len(hl2)])
	test['hl2_title'] = ' '.join(hl2_title[2:len(hl2)])

	print test


hl3_list = f3.readlines()
for hl3 in hl3_list:
	hl3_num = re.search(r'\d+\.\d+\.\d+', hl3)
	print hl3_num.group()
	test['hl3_num'] =hl3_num.group()

	hl3_title = re.findall(r'(\w+)', hl3)
	print ' '.join(hl3_title[2:len(hl3)])
	test['hl3_title'] = ' '.join(hl3_title[2:len(hl3)])

	print test



f2.close()
f3.close()
f4.close()
f5.close()



#for num in test_nums:
#	print num



#for title in test_titles:
	#print title

#for line in lines:
	# check for the stray character in line
	# if it exists
	# then push to temp
	# and pop on the next iteration
	#matchObj = re.match(r'(\d+\.\d+) (\w+)', line)
#	if matchObj:
#		print matchObj.group(0)

#print len(lines_new)	


'''
matchObj = re.search(r'(\d+\.\d+) (\d+)', line)

if matchObj:
	print matchObj.group()


	if matchObj:
		print matchObj.group()
	else:
		print "None!"


	matchObj = re.match(r'(\d+)', line.strip('\n'))
	if matchObj:
		print matchObj.group(0)
	else:
		print "No match!"'''

