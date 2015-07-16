from lxml import html
import requests
import re


def find_address(comment):
	m=re.search('<b>Permanent Address :</b>(.*)India<br>',comment)
	if not m:
		return False
	interesting= m.group(0)[26:-4]
	important=interesting.split(',')
	return {'s':important[len(important)-2],'c':important[len(important)-3]}

def fetch(roll_no):
	url='http://oa.cc.iitk.ac.in:8181/Oa/Jsp/OAServices/IITk_SrchRes1.jsp?typ=stud&numtxt='+str(roll_no)+'&sbm=Y'
	print 'Fetching %s for \n %s' % (url,roll_no)
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
	data['n']=name[1].strip()
	data['p']=program[1].strip()
	data['d']=department[1].strip()
	data['h']=hostel[1].strip()
	data['e']=str(email[0].strip())[:-11]
	data['b']=blood[1].strip()
	data['g']=gender[1].strip()
	data['c']=addrsss['c']
	data['s']=addrsss['s']
	return data