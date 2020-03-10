a = raw_input("enter network IP Address ")
a1=a.split('.')
oct0=format(int(a1[0]),'08b')
oct1=format(int(a1[1]),'08b')
oct2=format(int(a1[2]),'08b')
oct3=format(int(a1[3]),'08b')
ip_bin=[]
k=['.']
ip_bin=list(oct0)+k+list(oct1)+k+list(oct2)+k+list(oct3)


phy_net=int(input("Enter number of physical networks:"))
host=int(input("Enter number of hosts:"))

size=phy_net*host
if(size<(2**8)):
	print("Class C will be better")
elif(size<(2**16)):
	print("Class B will be better")
elif(size<(2**24)):
	print("Class A will be better")


r=0
while(2**r<phy_net):
	r=r+1
print("Number of subnets: "+str(2**r))




print("Given IP address is: ")
print("".join(ip_bin))


if(int(a1[0])>191 and int(a1[0])<223 and size<(2**8) ):
	print("subnetting in class C: ")
	mask=[]
	for i in range(35):
		if((i==8)or(i==17)or(i==26)):
			mask.append('.')
		elif(i<27+r):
			mask.append('1')
		else:
			mask.append('0')
	print("Mask is: ")
	print("".join(mask))
	subnet=[]			
	for i in range(35):
		if((i!=8)or(i!=17)or(i!=26)):
			if(ip_bin[i]==mask[i]):
				subnet.append(ip_bin[i])
			else:
				subnet.append('0')
		else:
			subnet.append('.')
	print("Subnet is : ")
	print("".join(subnet))
	oct_s0=[]
	oct_s1=[]
	oct_s2=[]
	oct_s3=[]	
	for i in range(35):
		if(i<8):
			oct_s0.append(subnet[i])
		elif(i>8 and i<17):
			oct_s1.append(subnet[i])
		elif(i>17 and i<26):
			oct_s2.append(subnet[i])
		elif(i>26 and i<35):
			oct_s3.append(subnet[i])
	o0=int("".join(oct_s0),2)
	o1=int("".join(oct_s1),2)
	o2=int("".join(oct_s2),2)
	o3=int("".join(oct_s3),2)		
	print(str(o0)+"."+str(o1)+"."+str(o2)+"."+str(o3))
	print("number of hosts in each subnet :"+str((2**(8-r)-2)))


elif(int(a1[0])>127 and int(a1[0])<192 and size<(2**16) ):
	print("subnetting in class B: ")
	mask=[]
	for i in range(35):
		if((i==8)or(i==17)or(i==26)):
			mask.append('.')
		elif(i<18+r):
			mask.append('1')
		else:
			mask.append('0')
	print("Mask is: ")
	print("".join(mask))
	subnet=[]			
	for i in range(35):
		if((i!=8)or(i!=17)or(i!=26)):
			if(ip_bin[i]==mask[i]):
				subnet.append(ip_bin[i])
			else:
				subnet.append('0')
		else:
			subnet.append('.')
	print("Subnet is : ")
	print("".join(subnet))
	oct_s0=[]
	oct_s1=[]
	oct_s2=[]
	oct_s3=[]	
	for i in range(35):
		if(i<8):
			oct_s0.append(subnet[i])
		elif(i>8 and i<17):
			oct_s1.append(subnet[i])
		elif(i>17 and i<26):
			oct_s2.append(subnet[i])
		elif(i>26 and i<35):
			oct_s3.append(subnet[i])
	o0=int("".join(oct_s0),2)
	o1=int("".join(oct_s1),2)
	o2=int("".join(oct_s2),2)
	o3=int("".join(oct_s3),2)		
	print(str(o0)+"."+str(o1)+"."+str(o2)+"."+str(o3))
	print("number of hosts in each subnet :"+str((2**(16-r)-2)))



elif(int(a1[0])>=0 and int(a1[0])<128 and size<(2**24) ):
	print("subnetting in class A: ")
	mask=[]
	for i in range(35):
		if((i==8)or(i==17)or(i==26)):
			mask.append('.')
		elif(i<9+r):
			mask.append('1')
		else:
			mask.append('0')
	print("Mask is: ")
	print("".join(mask))
	subnet=[]			
	for i in range(35):
		if((i!=8)or(i!=17)or(i!=26)):
			if(ip_bin[i]==mask[i]):
				subnet.append(ip_bin[i])
			else:
				subnet.append('0')
		else:
			subnet.append('.')
	print("Subnet is : ")
	print("".join(subnet))
	oct_s0=[]
	oct_s1=[]
	oct_s2=[]
	oct_s3=[]	
	for i in range(35):
		if(i<8):
			oct_s0.append(subnet[i])
		elif(i>8 and i<17):
			oct_s1.append(subnet[i])
		elif(i>17 and i<26):
			oct_s2.append(subnet[i])
		elif(i>26 and i<35):
			oct_s3.append(subnet[i])
	o0=int("".join(oct_s0),2)
	o1=int("".join(oct_s1),2)
	o2=int("".join(oct_s2),2)
	o3=int("".join(oct_s3),2)		
	print(str(o0)+"."+str(o1)+"."+str(o2)+"."+str(o3))
	print("number of hosts in each subnet :"+str((2**(24-r)-2)))
