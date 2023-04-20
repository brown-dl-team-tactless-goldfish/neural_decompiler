class Solution {
private:
    int countSetBits(int mask){
        int count=0;
        while(mask!=0){
            count += mask&1;
            mask/=2;
        }
        return count;
    }
public:
    int minimumXORSum(vector<int>& n1, vector<int>& n2) {
        int n = n1.size();
        vector<vector<long long>> dp(n,vector<long long>((1<<(n)),INT_MAX));
        for(int i=0;i<n;i++){
            dp[0][1<<i] = n1[0]^n2[i];
        }
        for(int i=1;i<n;i++){
            for(int mask=0;mask<(1<<n);mask++){
                int setBits = countSetBits(mask);
                if(setBits==i){
                    for(int j=0;j<n;j++){
                        if(!(mask & (1<<j))){
                            dp[i][mask+(1<<j)] = min(dp[i][mask+(1<<j)],dp[i-1][mask]+(n1[i]^n2[j]));
                        }
                    }
                }
            }
        }
        return dp[n-1][(1<<n)-1];
    }
};