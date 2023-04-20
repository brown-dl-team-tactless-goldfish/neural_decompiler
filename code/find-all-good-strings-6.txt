class Solution {
public:
    int mod = 1000000007;
    vector<int>lps;
    int m, n;
    string s1, s2, evil;
    int dp[501][51][2][2];
    int solve(int i, int matched, int left, int right){
        if(matched == m) return 0;
        if(i == n) return 1;
        if(dp[i][matched][left][right] != -1) return dp[i][matched][left][right];
        char from = left ? s1[i] : 'a';
        char to = right ? s2[i] : 'z';
        int res = 0;
        for(char c = from; c <= to; c++){
            int j = matched;
            while(j > 0 && evil[j] != c) j = lps[j - 1];
            if(c == evil[j]) j++;
            res += solve(i + 1, j, left && (c == from) , right && (c == to));
            res %= mod;
        }
        cout<<res<<endl;
        return dp[i][matched][left][right] = res;
    }
    int findGoodStrings(int n, string s1, string s2, string evil) {
        this->n = n;
        this->s1 = s1, this->s2 = s2, this->evil = evil;
        m = evil.size();
        memset(dp, -1, sizeof(dp));
        lps.resize(m, 0);
        int i = 1, j = 0;
        while(i < m){
            if(evil[i] == evil[j]){
                lps[i++] = ++j;
            }
            else{
                if(j != 0)
                    j = lps[j - 1];
                else i++;
            }
        }
        int ans = solve(0, 0, 1, 1);
        return ans;
    }
};