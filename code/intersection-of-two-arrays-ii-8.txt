int* intersect(int* nums1, int nums1Size, int* nums2, int nums2Size, int* returnSize){
    int *ans = malloc((nums1Size > nums2Size ? nums1Size : nums2Size) * sizeof(int));
    int cur = 0;
    
    int freq[1001] = {0}; 
    
    for (int i = 0; i < nums1Size; i++) {
        freq[nums1[i]]++;
    }
    
    for (int i = 0; i < nums2Size; i++) {
        if (freq[nums2[i]] != 0) {
            ans[cur++] = nums2[i];
            freq[nums2[i]]--;
        }
    }
    *returnSize = cur;
    return ans;
}