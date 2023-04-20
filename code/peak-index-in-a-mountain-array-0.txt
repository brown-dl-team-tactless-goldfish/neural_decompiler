

int peakIndexInMountainArray(int* arr, int arrSize){
    int start = 0;
    int end = arrSize-1;
    int mid;
    while(start!=end)
    {
        mid = (start+end)/2;
        if(arr[mid] > arr[mid+1]) // we are in decreasing part ans lies in left
        {
            end = mid;
        }
        else if(arr[mid+1]>arr[mid])
        {
            start = mid+1;
        }
    }
    return start;

}