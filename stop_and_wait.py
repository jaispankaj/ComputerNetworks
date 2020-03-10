import time
frames = int(input("Enter the number of frames"))
re = int(input("enter the lost packet number"))
tt = float(input("transmission time of each frame :"))
pt = float(input("propagation time :"))
eff = tt/(tt+2*pt)
j=0
for i in range(1,frames+1):
	j=j+1
	print("sender: frame "+str(i))
	time.sleep(tt+pt)
	print("receiver: frame "+str(i))
	time.sleep(pt)
	if(j%re == 0):
		print("nack")
		print("sender: frame "+str(i))
		time.sleep(tt+pt)
		print("receiver: frame "+str(i))
		time.sleep(pt)
		print("ack")
		j=j+1
	else:
		print("ack")
	i=i+1


total_frames= ((frames+(frames//re))//re)+frames
print("efficiecy :"+str(eff*100)+"%")
print("utilization : "+str(float(frames*100/total_frames)))