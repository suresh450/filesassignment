 
 
sm="module"
em="endmodule"
count=0
flag=0
fd=open("module.txt","r")
data=fd.readlines()
for line in data:
    print(line)
    if line.startswith(sm):
        flag=flag+1
    if (flag==1):
        count=count+1
    if line.startswith(em):
        break
print(count-2)
		
 
    