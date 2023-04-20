#define ll long long

class Solution {
public:
    int waysToSplit(vector<int>& nums) {
        ll n = nums.size(), pref[100005], mod = 1e9+7;;
        pref[0] = nums[0];
        for(int i = 1; i < n; i++) pref[i] = pref[i-1]+nums[i];
        int cnt = 0;
        for(int i = 0; i < n-2; i++) {
            ll left = pref[i];
            ll rest = pref[n-1]-pref[i];
            auto lb = lower_bound(pref+i+1,pref+n-1,2*left);
            auto ub = upper_bound(pref+i+1,pref+n-1,rest/2+left);
            if(ub-lb > 0) cnt += ub-lb; 
            cnt %= mod;
        }
        
        return cnt%mod;
    }
};