class Solution {
public:
    int knightDialer(int n) {
        if(n==1)return 10;
        int mod=1000000007;
        vector<long long int>cur(10,1),prev(10,1);
        for(int i=1;i<n;i++){
            cur[0]=(prev[4]+prev[6])%mod;
            cur[1]=(prev[8]+prev[6])%mod;
            cur[2]=(prev[7]+prev[9])%mod;
            cur[3]=(prev[8]+prev[4])%mod;
            cur[7]=(prev[2]+prev[6])%mod;
            cur[9]=(prev[2]+prev[4])%mod;
            cur[5]=0;
            cur[8]=(prev[1]+prev[3])%mod;
            cur[4]=(prev[3]+prev[9]+prev[0])%mod;
            cur[6]=(prev[1]+prev[7]+prev[0])%mod;
        
        prev=cur;
    }
        long long int ans=0;
            for(int i=0;i<10;i++){
         ans=(ans+cur[i])%mod;
     }
    return ans;
    }
};