#include<iostream>
using namespace std;

int main(){
	int str_size, parity_size=1,count,parity;
	
	cout<<"enter string size "<<endl;
	cin>>str_size;

	int a[str_size],i;
	cout<<"enter the data received( complete string including parity :  ";
	for(i=0;i<str_size;i++){
		cin>>a[i];
		}
	int msg_size = (str_size - parity_size)/parity_size;
	for(i=0;i<parity_size; i++){
		count=0;
		parity=0;
		for(int j=0;j<msg_size;j++){
			if(a[(i*msg_size)+j] == 1){
				count++;
				}
			}
		if(count%2!=0){
			parity=1;
			}
		if(parity == a[(str_size - parity_size)+i]){
			cout<<"msg "<<i+1<<" has no error"<<endl;
			}
		else{
			cout<<"msg "<<i+1<<" has error"<<endl;
			}
		}
	return 0;
	}