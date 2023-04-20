class Solution {
public:
    vector<long long> minOperations(vector<int>& nums, vector<int>& queries) {
        long long n = nums.size();
        sort(nums.begin(), nums.end());
        vector<long long> ps(n + 1), ss(n + 1), ans;
        for(int i=1; i<=n; i++) ps[i]  = ps[i - 1] + nums[i  - 1];
        for(int i=n-1; i>=0; i--) ss[i] = ss[i + 1] + nums[i];
        
        for(int q : queries) {
            long long pos = lower_bound(nums.begin(), nums.end(), q) - nums.begin();
            long long val = pos * q  - ps[pos] + ss[pos] - (n - pos) * q;
            ans.push_back(val);
        }
        return ans;
    }
};