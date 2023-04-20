#define MAX(a,b) ((a > b) ? a : b)

int findMaxLength(int* nums, int size){
    int max = 0, bl = 0, arr[2*size+1];    //balanced
    for(int i=0; i<2*size+1; i++)  arr[i] = -2;
    arr[size] = -1;
    
    for(int i=0; i<size; i++){
        if(nums[i])  bl++;
        else  bl--;
        if(arr[size+bl] < -1)
            arr[size+bl] = i;    //the leftist position that bl is this bl
        max = MAX(max, i - arr[size+bl]);
    }
    return max;
}