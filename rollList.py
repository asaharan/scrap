import unirest
from lxml import html
url = "http://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITK_Srch.jsp?typ=stud"
res = unirest.get(url)
# print res.body
tree = html.fromstring(res.body)
dep = tree.xpath("/html/body/form/table[1]/tr[4]/td[2]/select/option")
dep_list = []
for d in range(2,len(dep)):

	b = tree.xpath("/html/body/form/table[1]/tr[4]/td[2]/select/option["+str(d)+"]/@value")
	dep_list.append(b[0])
	# print b[0]

print dep_list

finalDepList = []
rollNumberList = []
for d in dep_list:
	url = "http://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStudRoll.jsp?recpos=0&selstudrol=&selstuddep="+d+"&selstudnam="
	res = unirest.get(url)
	tree = html.fromstring(res.body)
	noe = tree.xpath("/html/body/form/div/b[3]/text()")
	# print noe
	if len(noe)>0:
		finalDepList.append({"headCount":noe[0], "dep":d})


print finalDepList		


for d in finalDepList:
	dep = d["dep"]
	headCount = d["headCount"]
	for i in range(0,int(float(headCount)),12):
		url = "http://oa.cc.iitk.ac.in/Oa/Jsp/OAServices/IITk_SrchStudRoll.jsp?recpos="+str(i)+"&selstudrol=&selstuddep="+dep+"&selstudnam="
		res = unirest.get(url)
		tree = html.fromstring(res.body)
		aulade = tree.xpath("/html/body/form/table[2]/tr")
		# print len(aulade)
		londe = len(aulade)
		for j in range(2,londe+1):
			rollNo = tree.xpath("/html/body/form/table[2]/tr["+str(j)+"]/td[1]/a/text()")
			rollNumberList.append(rollNo)
			if rollNo == []:
				print d, i, j

	print rollNumberList




