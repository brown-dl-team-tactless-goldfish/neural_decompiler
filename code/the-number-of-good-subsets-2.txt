class Solution {
public:     
    const int mod = 1e9+7;
    
    int primes[11] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 27, 29};
    
    int numberOfGoodSubsets(vector<int>& nums) {        
        int cnts[31] = {};
        bool showed[31] = {};
        int factorstmp[31] = {};
        
        for (int i = 0; i < nums.size(); i++){
            int n = nums[i];

            if (showed[n]) {
                if (cnts[n]) cnts[n]++;
                
                continue;
            }
            
            showed[n] = true;
            
            int mask = 0;
            for (int j = 0; j < 11; j++) {
                if (!(n%primes[j])) {
                    n /= primes[j];
                    if (!(n%primes[j])) goto next;
                    
                    mask |= (1<<j);
                }
                
                if (n == 1) break;
            }
            cnts[nums[i]]++;
            factorstmp[nums[i]] = mask;
            
            next:;
        }
        
        vector<int> factors;
        vector<int> numsCnts;
        
        for (int i = 2; i < 31; i++){
            if (cnts[i]) {
                factors.push_back(factorstmp[i]);
                numsCnts.push_back(cnts[i]);
            }
        }
        
        vector<int> dp[numsCnts.size()];
        for (int i = 0; i < numsCnts.size(); i++)
            dp[i].resize(2048, -1);
        
        if (cnts[1]){
            long long sum = 0;
            for (int i = 1; i <= cnts[1]; i++) sum = ((sum<<1)+1)%mod;
            
            return (sum+1)*dfs(0, 0, factors, numsCnts, dp)%mod;
        }
        
        return dfs(0, 0, factors, numsCnts, dp);
    }
    
    long long dfs(int i, int mask, vector<int>& factors, vector<int>& numsCnts, vector<int> dp[]){
        if (i == numsCnts.size()) return mask != 0;
        
        if (dp[i][mask] != -1) return dp[i][mask];
        
        long long res = dfs(i+1, mask, factors, numsCnts, dp);
        int maskcpy = mask;
        
        for (int j = 0; j < 11; j++){
            if ((factors[i]>>j)&1){
                if ((mask>>j)&1) return dp[i][mask] = res;
            
                maskcpy |= (1<<j);
            }
        }
        
        return dp[i][mask] = (res+(numsCnts[i]*dfs(i+1, maskcpy, factors, numsCnts, dp)%mod))%mod;
    }
    
};