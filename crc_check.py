msg="11010111101100100"
divisor="1011"
n=len(divisor)-1
padded_msg = list(msg)
for bit_m in range(len(padded_msg)-n):
	if(padded_msg[bit_m] == '1'):
		for bit_d in range(len(divisor)):
			if(padded_msg[bit_m+bit_d]==divisor[bit_d]):
				d=0
			else:
				d=1
			padded_msg[bit_m+bit_d] =str(d)
if '1' in padded_msg:
	print("error")
else:
	print("no error")