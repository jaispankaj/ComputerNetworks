#include<iostream>
using namespace std;

int main(){
	int str_size, chunk_size=4, count, parity;
	
	cout<<"enter sender data size ( only data size without redundency bit) "<<endl;
	cin>>str_size;
	int padding_size = 4 - str_size%4;

	int a[str_size+padding_size],i;
	cout<<"enter the data :  ";
	for(i=0;i<str_size;i++){
		cin>>a[i];
		}
	for(i=str_size;i<str_size+padding_size;i++){
		a[i] = 0;
		}
	
	int red_bit[chunk_size];

	cout<<"final data after padding : ";
	for(i=0;i<str_size + padding_size;i++){
		cout<<a[i];
		}
	cout<<endl;

	cout<<"LRC bits are :";
	for(i=0;i<chunk_size; i++){
		count=0;
		parity=0;
		for(int j=i;j<(str_size + padding_size);j=j+chunk_size){
			if(a[j] == 1){
				count++;
				}
			}
		if(count%2!=0){
			parity=1;
			}
		red_bit[i] = parity;
		cout<<red_bit[i];
		}
	
	
	return 0;
	}