class Solution {
public:
    long long countGood(vector<int>& nums, int k) {
        long long i = 0, ans = 0, count = 0, n = nums.size();
        unordered_map<long long, long long> m;
        
        for(int j=0; j<n; j++) {
            m[nums[j]]++;
            if(m[nums[j]] > 1) count += m[nums[j]]  - 1;
            
            while(i <= j && count >= k) {
                ans += n - j;
                m[nums[i]]--;
                if(m[nums[i]] >= 1) count -= m[nums[i]];
                i++;
            } 
        }
        return ans;
    }
};