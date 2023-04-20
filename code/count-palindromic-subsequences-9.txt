class Solution {
public:
    long long dp[10001][10][10][6];
    long long mod = 1000000007;
    
    long long solve(string &s, long long idx, long long first, long long second, long long cnt){
        int n = s.size();
        if(idx == n){
            if(cnt == 5) return 1;
            return 0;
        }
        if(dp[idx][first][second][cnt] != -1) return dp[idx][first][second][cnt];
        
        long long inc = 0, exc = 0, val = s[idx]-'0';
        if(cnt == 0){
            inc += solve(s, idx+1, val, second, cnt+1); 
        }
        else if(cnt == 1){
            inc += solve(s, idx+1, first, val, cnt+1); 
        }
        else if(cnt == 2){
            inc += solve(s, idx+1, first, second, cnt+1); 
        }
        else if(cnt == 3){
            if(val == second) inc += solve(s, idx+1, first, second, cnt+1); 
        }
        else if(cnt == 4){
            if(val == first) inc += solve(s, idx+1, first, second, cnt+1); 
        }
        exc += solve(s, idx+1, first, second, cnt);
        return dp[idx][first][second][cnt] = (inc%mod+exc%mod)%mod;
    }

    int countPalindromes(string s) {
        memset(dp, -1, sizeof(dp));
        return solve(s, 0, 0, 0, 0);
    }
};