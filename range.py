import main
import json
import timeit
# import math
start_roll_no=input('Enter first roll no:')
last_roll_no=input('Enter last roll no:')

file_name=raw_input('File in which data should be stored [default is data.json]:')
if file_name=='':
	file_name='data.json'
elif len(file_name.split('.'))<2:
	file_name+='.json'
data={}

if start_roll_no>last_roll_no:
	tmp=start_roll_no
	start_roll_no=last_roll_no
	last_roll_no=tmp
roll_no=start_roll_no

start = timeit.default_timer()
while roll_no<=last_roll_no:
	if main.fetch(roll_no):
		data[roll_no]=main.fetch(roll_no)
	roll_no+=1

stop = timeit.default_timer()
print 'Time take is '+str(int(stop - start))+' For '+str(last_roll_no - start_roll_no+1)+' persons'

print 'Data is stored in', file_name
json_file=open('data/'+file_name,'w')
json_file.write(json.dumps(data,sort_keys=True,indent=4,separators=(',',': ')))