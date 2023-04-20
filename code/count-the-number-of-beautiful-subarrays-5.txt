class Solution {
public:
    long long beautifulSubarrays(vector<int>& nums) {

        long long ans=0;
        unordered_map<int,int> mp;
        mp[0]=1;

        int val=0;
        for(auto ele:nums){
            val = val^ele;

            if(mp.find(val) != mp.end()){
                ans+= mp[val];
            }
            mp[val]++;
        }
        return ans;
    }
};