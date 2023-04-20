class Solution {
private:
    int n,mod=1000000000+7;
    vector<vector<int>>mem;
    int solve(string &s,int index,int prev,vector<bool>&seen){
        if(index==n){
            return 1;
        } else if(mem[index][prev]!=-1){
            return mem[index][prev];
        } else {
            int ans=0;
            if(s[index]=='D'){
                for(int i=0;i<prev;i++){
                    if(!seen[i]){
                        seen[i]=true;
                        ans=(ans%mod+solve(s,index+1,i,seen)%mod)%mod;
                        seen[i]=false;
                    }
                }
            } else {
                for(int i=prev+1;i<=n;i++){
                    if(!seen[i]){
                        seen[i]=true;
                        ans=(ans%mod+solve(s,index+1,i,seen)%mod)%mod;
                        seen[i]=false;
                    }
                }
            }
            return mem[index][prev]=ans;
        }
    }
public:
    int numPermsDISequence(string &s) {
        n=s.size();
        int ans=0;
        mem=vector<vector<int>>(n+1,vector<int>(n+1,-1));
        vector<bool>seen(n+1,false);
        for(int i=0;i<=n;i++){
            seen[i]=true;
            ans=(ans%mod+solve(s,0,i,seen)%mod)%mod;
            seen[i]=false;
        }
        return ans;
    }
};