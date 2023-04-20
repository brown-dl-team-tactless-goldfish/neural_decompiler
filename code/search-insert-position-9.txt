int searchInsert(int* nums, int numsSize, int target){
    int low = 0, high = numsSize-1, mid = (high+low)/2;
    
    while(low <= high){
        if(nums[mid] == target){
            return mid;
        }    
        else if(nums[mid] < target){
            low = mid+1;
            mid = (high+low)/2;
        }
        else{
            high = mid-1;
            mid = (high+low)/2;
        }    
    }
    
    return low;
}