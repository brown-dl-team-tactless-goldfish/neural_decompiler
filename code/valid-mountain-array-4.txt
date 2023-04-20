bool validMountainArray(int* arr, int arrSize){
int i,m,flag=0;

if (arrSize<3||arr[0]>arr[1])
    return false;

for(i=0;i<arrSize-1;i++)
{ 
    if(arr[i]>=arr[i+1])
    { 
    flag=1;
     if(arr[i]==arr[i+1])
            return false;
     if (arr[i]>arr[i+1])
        for( m=i+1;m<arrSize-1;m++) 
            if(arr[m]<=arr[m+1])
                return false;
    }
}

if(flag==1)
	return true;
	else return false;
}