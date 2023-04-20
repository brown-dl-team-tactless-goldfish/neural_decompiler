class Solution {
public:
    int N;int K,ml;
    int dp[1001][1001];
    int mod=1e9+7;
    int recur(string& s,int startsAt,int left){
        if(dp[startsAt][left]!=-1)return dp[startsAt][left];
        if(left==1){
            return 1;
        }
        // pr(startsAt);
        int count=0;
        for(int i=startsAt;i<N-1;i++){
            if(i-startsAt+1>=ml && (N-1-i)>=ml && s[i]=='c' && s[i+1]=='p'){
                count=(count+recur(s,i+1,left-1))%mod;
            }
        }
        dp[startsAt][left]=count%mod;
        return count;
    }
    int beautifulPartitions(string s, int k, int minLength) {
        N=s.length();K=k;ml=minLength;
        for(int i=0;i<N+1;i++){
            for(int j=0;j<N+1;j++){
                dp[i][j]=-1;
            }
        }
        for(int i=0;i<N;i++){
            if(s[i]=='2'||s[i]=='3'||s[i]=='5'||s[i]=='7'){
                s[i]='p';
            }
            else{
                s[i]='c';
            }
        }
        if(s[0]=='c' || s[N-1]=='p')return 0;
        return recur(s,0,k);
    }
};