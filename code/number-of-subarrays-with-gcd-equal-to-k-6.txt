class Solution {
public:
    int subarrayGCD(vector<int>& nums, int k) {
        int n = nums.size(), res = 0;
        if(n == 1) return nums[0] == k;
        
        for(auto i = 0; i < n-1; i++){
            int a = nums[i];
            if(a == k) res++;
            
            for(auto j = i+1; j < n; j++){
                a = __gcd(nums[j], a);
                if(a == k) res++;
            }
        }
        if(nums[n-1] == k) res++;
        
        return res;
    }
};