data=raw_input("Enter the data stream : ")
data_l=list(data)

count=0
for i in range(len(data_l)):
	if(count==5):
		data_l.insert(i,'0')
	if(data_l[i]=='1'):
		count=count+1
	else:
		count=0
print("bit stuffed data : "+"".join(data_l))

data_o=[]
for i in range(len(data_l)):
	if(count==5):
		i+=1
	if(data_l[i]=='1'):
		count=count+1
	else:
		count=0
	data_o.append(data_l[i])
print("bit de-stuffed data : "+"".join(data_o))