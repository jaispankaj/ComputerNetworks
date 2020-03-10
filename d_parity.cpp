#include<iostream>
using namespace std;

int main(){

	int str_size, chunk_size, k=0,count, parity,i;
	cout<<"enter the complete string size and chunk size : ";
	cin>>str_size>>chunk_size;

	if(str_size%chunk_size !=0){
		cout<<"enter valid chunk size and string size";
		return -1;
		}

	int a[str_size];
	cout<<"enter the string :";
	for(i=0;i<str_size;i++){
		cin>>a[i];
		}
	
	//vertical parity is at end of string and horizontal parity at end of each chunk
	int no_chunk = (str_size-chunk_size)/(chunk_size+1);
	int hor_par_giv[no_chunk];
	int ver_par_giv[chunk_size];
	
	for(i=0;i<chunk_size;i++){
		ver_par_giv[i] = a[str_size - chunk_size + i];
		}
	k=chunk_size;
	for(i=0;i<no_chunk;i++){
		
		hor_par_giv[i] = a[k];
		k=chunk_size + k +1;
		}
	int j;
	k=0;
	int hor_par_obs[no_chunk];
	int ver_par_obs[chunk_size];
	for(i=0;i<no_chunk;i++){
		count=0;
		parity= 0;
		for(j=0;j<chunk_size;j++){
			if(a[(i*chunk_size)+k+j]==1){
				count++;
				}
			}
		k=1;
		if(parity%2!=0){
			parity = 1;
			}
		hor_par_obs[i]=parity;
		}

	for(i=0;i<chunk_size;i++){
		count=0;
		parity=0;
		for(j=i;j<(str_size-chunk_size);j=j+chunk_size+1){
			if(a[j] == 1){
				count++;
				}
			}
		if(count%2!=0){
			parity=1;
			}	
		ver_par_obs[i]=parity;
		}
	cout<<"given horizontal: ";
	for(i=0;i<no_chunk;i++){
		cout<<hor_par_giv[i];
		}
	cout<<endl;
	cout<<"obs horizontal: ";
	for(i=0;i<no_chunk;i++){
		cout<<hor_par_obs[i];
		}
	cout<<endl;
	cout<<"given vertical: ";
	for(i=0;i<chunk_size;i++){
		cout<<ver_par_giv[i];
		}
	cout<<endl;
	cout<<"obs vertical: ";
	for(i=0;i<chunk_size;i++){
		cout<<ver_par_obs[i];
		}
	cout<<endl;

	return 0;
}



















