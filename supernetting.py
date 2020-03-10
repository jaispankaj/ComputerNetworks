host=int(input("Enter the number of host devices: "))

if(host<=(2**8)-2):
	print("1 class C can host required number of devices")
elif(host<((2**16)-(2**9))):
	print("supernet class C  ")
	if(host%254==0):
		d=(host//254)
	else:
		d=(host//254)+1
	print("# contiguous class C required: "+str(d))

elif(host<((2**24)-(2**9))):
	print("supernet class B  ")
	if(host%((2**16)-2)==0):
		d=(host//((2**16)-2))
	else:
		d=(host//((2**16)-2))+1
	print("# contiguous class B required: "+str(d))

elif(host<((2**32)-(2**9))):
	print("supernet class A  ")
	if(host%((2**16)-2)==0):
		d=(host//((2**24)-2))
	else:
		d=(host//((2**24)-2))+1
	print("# contiguous class A required: "+str(d))
else:
	print("enter proper number of hosts")


	
	