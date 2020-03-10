import time
frames = int(input("Enter the number of frames"))
re = int(input("enter the lost packet number"))
window = int(input("Enter window size"))
#tt= float(input("transmission time of each frame :"))
#pt= float(input("propagation time :"))

sending_packet=1
sent_packet=0
count=1
while(sending_packet<=frames+window):
	if(count==re+window and sending_packet-window<=frames):
		print("resending packet "+str(sending_packet - window))
		sent_packet+=1
		count=window+1
	else:
		count+=1
		if(sending_packet<=frames):
			print("sending packet "+str(sending_packet))
			sent_packet+=1
		sending_packet+=1
print(sent_packet)