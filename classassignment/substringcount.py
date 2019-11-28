sub="EDFFX2AD"
s1="DFFQXLAD"
count=0
e=0
f=open("substring.txts","rt")
d=f.readlines()
print(len(d),d)
i=1
for l in d:
	print(l)
	if(l.startswith(sub)):
		print(l.count(sub),sub)
		count=count+1
	if(l.startswith(s1)): 
		print(l.count(s1),s1)
		e=e+1
print(count)
print(e)
		
		
 
