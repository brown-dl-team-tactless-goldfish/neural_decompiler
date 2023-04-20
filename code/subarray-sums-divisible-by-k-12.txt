class Solution {
public:
    int subarraysDivByK(vector<int>& nums, int k) {
        vector<int> pre (k, 0);
        int cur_sum = 0;
        for(int x : nums){
            cur_sum += (x % k + k) % k;
            pre[cur_sum % k]++;
        }
        int res = pre[0];
        for(int c : pre){
            res += (c * (c -1)) / 2;
        }
        return res;
    }
};