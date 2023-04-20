class Solution {
public:
    int subarrayLCM(vector<int>& nums, int k) {
        long long ans=0,mul=1;
        for(int i=0;i<nums.size();i++){
            for(int j=i;j<nums.size();j++){
                mul = lcm(mul,nums[j]);
                if(mul == k) ans++;
                if(mul>k) break;
            }
            mul=1;
        }
        return ans;
    }
};