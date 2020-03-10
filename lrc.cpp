#include<iostream>
using namespace std;

int main(){
	int str_size, chunk_size, count, parity;
	cout<<"enter redundancy bit size : ";
	cin>>chunk_size;
	cout<<"enter sender data size (including with redundency bit) "<<endl;
	cin>>str_size;
	

	int a[str_size],i;
	cout<<"enter the data :  ";
	for(i=0;i<str_size;i++){
		cin>>a[i];
		}
	

	for(i=0;i<chunk_size; i++){
		count=0;
		parity=0;
		for(int j=i;j<(str_size-chunk_size);j=j+chunk_size){
			if(a[j] == 1){
				count++;
				}
			}
		if(count%2!=0){
			parity=1;
			}
		
		if(parity != a[str_size - chunk_size + i]){
			cout<<"column "<<i+1<<" has error"<<endl;
			}
		}
	
	
	return 0;
	}