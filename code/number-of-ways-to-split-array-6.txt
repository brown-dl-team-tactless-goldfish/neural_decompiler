class Solution {
public:
   int waysToSplitArray(vector<int>& nums) 
    {
        int valid_split=0;
        long long right_sum=0;
        long long left_sum =0;
        
        for(int i=0; i<nums.size(); i++) 
            right_sum += nums[i];
        
        for(int i=0; i<nums.size()-1; i++)
        {
            left_sum += nums[i];  
            right_sum -= nums[i]; 
            
            if(left_sum >= right_sum) 
                valid_split++; 
        }
        return valid_split;    
    }
};