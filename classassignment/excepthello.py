
s="hello"
f=open("hello.txt","r")
w=open("w.txt","w")
d=f.readlines()
for l in d:
	#print(l)
	if not s in l :
		print(l)
