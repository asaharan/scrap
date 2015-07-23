import unirest
import main
import json
callbacks=0
data=[]
count=0
jatha=25
def callme(response):
	global callbacks
	global data
	data.append(main.fetch(response.body))
	callbacks+=1
	you_handle()

def done_fetching():
	global file_name
	global data
	data=sorted(data,key=lambda k:k['r'])
	# print data
	print len(data)
	# print 'Data is stored in data/',file_name
	print 'done'
	json_file=open('data/'+file_name,'w')
	json_file.write(json.dumps(data,sort_keys=True,indent=4,separators=(',',': ')))

def you_handle():
	global count
	global data
	if callbacks>=total:
		done_fetching()
	count+=1
	if count==1:
		count=jatha-1
		for v in range(0,jatha):
			roll_no=start_roll_no+v
			url='http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes1.jsp?typ=stud&numtxt='+str(roll_no)+'&sbm=Y'
			unirest.get(url,callback=callme)
			print 'init ', roll_no, v
	elif count<total:
		roll_no=start_roll_no+count
		url='http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes1.jsp?typ=stud&numtxt='+str(roll_no)+'&sbm=Y'
		unirest.get(url,callback=callme)
		print 'sent for', roll_no

start_roll_no=input('Enter first roll no:')
last_roll_no=input('Enter last roll no:')
file_name=raw_input('File in which data should be stored [default is data.json]:')
if file_name=='':
	file_name='data.json'
elif len(file_name.split('.'))<2:
	file_name+='.json'

unirest.timeout(50000)

if start_roll_no>last_roll_no:
	tmp=start_roll_no
	start_roll_no=last_roll_no
	last_roll_no=tmp
total = last_roll_no - start_roll_no+1
you_handle()

# print 'fetching data of '+str(last_roll_no - start_roll_no+1)+' persons'