
f=open("hello.txt","r")
w=open("comment.txt","w")
d=f.readlines()
for l in d:
	if  not l.startswith("#"):
		print(l)
