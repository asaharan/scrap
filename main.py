from lxml import html
import requests
import re

notavailable='Not available'

def find_address(comment):
	m=re.search('<b>Permanent Address :</b>(.*)India<br>',comment)
	if not m:
		return False
	interesting= m.group(0)[26:-4]
	important=interesting.split(',')
	return {'s':important[len(important)-2],'c':important[len(important)-3]}

def fetch(roll_no):
	url='http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes1.jsp?typ=stud&numtxt='+str(roll_no)+'&sbm=Y'
	print 'Fetching info for %s' % (roll_no)
	page = requests.get(url)

	page_text=page.text.strip()
	# html_file.write(page_text)
	tree = html.fromstring(page_text)
	#now scrap
	name=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[1]/text()')
	program=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[2]/text()')
	department=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[3]/text()')
	hostel=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[4]/text()')
	email=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[5]/a/text()')
	blood=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[6]/text()')
	gender=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/p[7]/text()')
	location=tree.xpath('/html/body/form/table/tr/td/table/tr/td/table/tr[3]/td/div/center/table/tr/td[2]/comment()')


	addrsss=find_address(str(location[0]))


	data={}
	try:
		data['n']=name[1].strip()
	except Exception, e:
		data['n']=notavailable
	try:
		data['p']=program[1].strip()
	except Exception, e:
		data['p']=notavailable
	try:
		data['d']=department[1].strip()
	except Exception, e:
		data['d']=notavailable
	try:
		data['h']=hostel[1].strip()
	except Exception, e:
		data['h']=notavailable
	try:
		data['e']=str(email[0].strip())[:-11]
	except Exception, e:
		data['e']=notavailable
	try:
		data['b']=blood[1].strip()
	except Exception, e:
		data['b']=notavailable
	try:
		data['g']=gender[1].strip()
	except Exception, e:
		data['g']=notavailable
	try:
		data['c']=addrsss['c']
	except Exception, e:
		data['c']=notavailable
	try:
		data['s']=addrsss['s']
	except Exception, e:
		data['s']=notavailable
	return data
