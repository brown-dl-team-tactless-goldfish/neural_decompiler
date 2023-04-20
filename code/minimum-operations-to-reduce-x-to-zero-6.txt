class Solution {
public:
    int findMaxSub(vector<int>& nums, int k) {
        int sum = 0, maxi = 0;
        unordered_map<int, int> m;
        
        for (int i=0; i<nums.size(); i++) {
            sum += nums[i];
            
            if (sum == k)
                maxi = i+1;
            
            if (m.find(sum) == m.end())
                m[sum] = i;
            
            if (m.find(sum - k) != m.end())
                maxi = max(maxi, i - m[sum-k]);
        }
        return maxi;
    }
    
    int minOperations(vector<int>& nums, int x) {
        if ((nums[0] > x) && (nums[nums.size()-1] > x))
            return -1;
        
        int sum = 0;
        for (auto a : nums)
            sum += a;
        
        if (sum == x) return nums.size();
        
        int res = findMaxSub(nums, sum-x);
        return res <= 0 ? -1 : nums.size() - res;
    }
};