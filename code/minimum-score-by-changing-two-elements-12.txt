class Solution 
{
public:
    int minimizeSum(vector<int>& nums) 
    {
        int n=nums.size();
        sort(nums.begin(), nums.end());
        
        //case-1 make first two elements as maximum element 
        int high1 = nums[n-1] - nums[2]; 
        
        //case-2 make last two elements  as minimum element
        int high2 = nums[n-3] - nums[0];
        
        //case-3 make 1st and last position element as 2nd minimum element or 2nd maximum element
        int high3 = nums[n-2] - nums[1];
        
        return min({high1, high2, high3});        
    }
};