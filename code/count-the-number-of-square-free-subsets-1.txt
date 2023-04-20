class Solution {
public:
    int squareFreeSubsets(vector<int>& nums) {
        map<long long, long long> cnt;
        const long long mod = 1e9+7;
        for(long long x:nums){
            if(x%4==0 || x%9==0 || x==25) continue;
            for(auto& [y, n] : cnt)
                if(gcd(x, y) == 1) cnt[x*y] = (cnt[x*y]+n) % mod;
            cnt[x]++;
        }
        long long sum = 0;
        for(auto [x,n] : cnt) sum += n;
        return sum % mod;
    }
};