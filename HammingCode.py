msg="1101"
giv_msg=list(msg)
r=0
while((2**r)<len(msg)+r+1):
	r+=1
r1=0
r2=0
r3=0
padded_msg=[]
k=0
j=0
count=[]
for i in range(1,len(msg)+r+1):
	if(i== 2**k):
		k+=1
		padded_msg.append(r1)
	else:
		padded_msg.append(msg[j])
		j+=1
print(padded_msg)
for i in range(r):
	if 
		