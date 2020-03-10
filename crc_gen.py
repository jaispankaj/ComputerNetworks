msg="11010011101100"
divisor="1011"
n=len(divisor)-1
padding_bit = '0'*n
padded_msg =list(msg+padding_bit)
for bit_m in range(len(msg)):
	if(padded_msg[bit_m] == '1'):
		for bit_d in range(len(divisor)):
			if(padded_msg[bit_m+bit_d]==divisor[bit_d]):
				d=0
			else:
				d=1
			padded_msg[bit_m+bit_d] =str(d)
print((padded_msg[:]))