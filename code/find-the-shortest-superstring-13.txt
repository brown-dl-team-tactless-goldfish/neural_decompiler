class Solution {
public:
    vector<int>len;
    vector<vector<int>>overlap;
    vector<vector<int>>dp;
    int n;
    map<pair<int, int>, int>mp;
    int solve(int idx, int mask){
        if(mask == (1 << n) - 1) return 0;
        if(dp[idx][mask] != -1)return dp[idx][mask];
        dp[idx][mask] = INT_MAX;
        for(int i = 0; i < n; i++){
            if((mask&(1 << i)) == 0){
                int temp = len[i] - overlap[idx][i] + solve(i, mask|(1 << i));
                if(temp < dp[idx][mask]){
                    dp[idx][mask] = temp;
                    mp[{idx, mask}] = i;
                }
            }
        }
        return dp[idx][mask];
    }
    string shortestSuperstring(vector<string>& A) {
        n = A.size();
        len.resize(n, 0);
        overlap.resize(n, vector<int>(n, 0));
        dp.resize(n, vector<int>((1 << n) + 1, -1));
        for(int i = 0; i < n; i++){
            len[i] = A[i].size();
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if(i != j){
                    int m = min(len[i], len[j]);
                    for(int k = m; k >= 0; k--){
                        if(A[i].substr(len[i] - k) == A[j].substr(0, k)){
                            overlap[i][j] = k;
                            break;
                        }
                    }
                }
            }
        }
        int mlen = INT_MAX;
        int idx = 0;
        for(int i = 0; i < n; i++){
            int temp = len[i] + solve(i, (1 << i));
            //cout<<temp<<endl;
            if(temp < mlen){
                mlen = temp;
                idx = i;
            }
        }
        string ans = A[idx];
        int mask = 1 << idx;
        for(int i = 1; i < n; i++){
            int x = idx;
            idx = mp[{idx, mask}];
            ans += A[idx].substr(overlap[x][idx]);
            mask |= (1 << idx); 
        }
        return ans;
    }
};