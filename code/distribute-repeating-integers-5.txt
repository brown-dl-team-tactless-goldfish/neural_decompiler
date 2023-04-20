class Solution {
public:
    
    int m, n;
    vector<int> a;
    vector<int> b;
    vector<vector<int> > dp;
    vector<int> cache;
    
    bool solve(int idx, int mask) {
        if(mask == (1 << m) - 1)
            return 1;
        
        if(idx == n)
            return 0;
        
        if(dp[idx][mask] != -1)
            return dp[idx][mask];
        
        for(int i = mask + 1; i < (1 << m); ++i) {
            if(mask != (mask & (i))) continue;
            
            if(a[idx] >= cache[i] - cache[mask] && solve(idx + 1, i)) {
                return dp[idx][mask] = true;
            }
        }
        
        return dp[idx][mask] = solve(idx + 1, mask);
    }
    
    
    bool canDistribute(vector<int>& nums, vector<int>& b) {
        
        unordered_map<int, int> mp;
        for(int x: nums) {
            mp[x] += 1;
        }
        for(auto p: mp)
            a.push_back(p.second);
        
        this->b = b;
        this->m = b.size();
        this->n = a.size();
        
        dp.clear(); dp.resize(n, vector<int> ((1<<m), -1));
        cache.clear(); cache.resize(1024, 0);
        
        for(int mask = 0; mask < (1 << m); ++mask) {
            for(int i = 0; i < m; ++i) {
                if(mask & (1 << i)) {
                    cache[mask] += b[i];
                }
            }
        }
        
        return solve(0, 0);
    }
};