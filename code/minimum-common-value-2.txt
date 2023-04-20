int getCommon(int* nums1, int nums1Size, int* nums2, int nums2Size){
    int b = -1;
    for(int i = 0; i < nums1Size;i++){
        int a = nums1[i];
        int s = 0, e = nums2Size - 1, mid = s + (e-s)/2;
        while(s<=e){
            if(nums2[mid] == a){
                return a;
            }
            else if(nums2[mid] < a){
                s = mid +1;
            }
            else{
                e = mid-1;
            }
            mid = s + (e-s)/2;
        }
    }
    return b;
}