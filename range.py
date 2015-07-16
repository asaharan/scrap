import main
import json

json_file=open('data.json','w')
# html_file=open('ss.html','w')
start_roll_no=input('Enter first roll no:')
last_roll_no=input('Enter last roll no:')
data={}

if start_roll_no>last_roll_no:
	tmp=start_roll_no
	start_roll_no=last_roll_no
	last_roll_no=start_roll_no
roll_no=start_roll_no
while roll_no!=last_roll_no:
	data[roll_no]=main.fetch(roll_no)
	roll_no+=1

json_file.write(json.dumps(data,sort_keys=True,indent=4,separators=(',',': ')))