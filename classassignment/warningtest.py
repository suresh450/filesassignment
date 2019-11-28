s="warning"
c1=0
c2=0
f=open("log1.txt","r")
d=f.readlines()
for l in d:
	if s in l:
		#print(l.count(s))
		c1=c1+1
print("Old Warning count 1log.txt:",c1)
f=open("log2.txt","r")
e=f.readlines()
for s in e:
	if s in l:
		#print(l.count(s))
		c2=c2+1
print("new Warning count 1log.txt:",c2)
if (c1>c2):
	print("build not promoted")
else:
	print("build is promoted")

	
