import re
st='<!--<p><b>Local Address :</b>Not Available<br>Not Available<br>\
		Phone no:Not Available<br>Mobile no:Not Available</P>\
		<p><b>Permanent Address :</b>Vinod Kumar<br>Village-Mattuwala,P.O Dhudhianwali,Sirsa,Haryana,India<br>\
  		Phone no:9467957654<br>Mobile no:Not Available</P>\
                <p><a href="Stff_Addr.jsp?typ=stud&pfno=13096">Address</a></p>-->'
m=re.search('<b>Permanent Address :</b>(.*)India<br>',st)
if m:
	print m.group(0)
else:
	print 'Not found'