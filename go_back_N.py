import time
frames = int(input("Enter the number of frames"))
re = int(input("enter the lost packet number"))
window = int(input("Enter window size"))
#tt= float(input("transmission time of each frame :"))
#pt= float(input("propagation time :"))

frames_ar=[]
for i in range(1,frames+1):
	frames_ar.append(i)
sent=[]
trans=[]
trans_start=0
count=0
while(len(sent) != frames-1):
	if(frames - trans_start >= window):
		trans=frames_ar[trans_start:trans_start+window]
	else:
		trans=frames_ar[trans_start:]
		
	count=count+1
	if(count%re!=0):
		sent.append(trans[0])
		trans_start=trans_start+1
	else:
		count=count+window-1
	print(trans)
print(count)
		
