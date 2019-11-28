count=0
fd = open("abc.txt","r")
data=fd.readlines()
for line in data:
    words = line.split( )
    print(words)
    count = count+len(words)
print(count)