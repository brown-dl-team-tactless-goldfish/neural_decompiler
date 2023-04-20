class Solution {
private:
    vector<vector<int>>mem;
    vector<int>prefix;
    int solve(vector<int>&prefix,int index,int p){
        if(index==prefix.size()-1){
            if(p==0){
                return prefix[index];
            } else {
                return -prefix[index];
            }
        } else if(mem[index][p]!=-1){
            return mem[index][p];
        } else {
            if(p==0){
                int ans1=prefix[index]+solve(prefix,index+1,!p);
                int ans2=solve(prefix,index+1,p);
                return mem[index][p]=max(ans1,ans2);
            } else {
                int ans1=-prefix[index]+solve(prefix,index+1,!p);
                int ans2=solve(prefix,index+1,p);
                return mem[index][p]=min(ans1,ans2);
            }
        }
    }
public:
    int stoneGameVIII(vector<int>& stones) {
        int n=stones.size();
        prefix=vector<int>(n+1,0);
        mem=vector<vector<int>>(n,vector<int>(2,-1));
        for(int i=1;i<prefix.size();i++){
            prefix[i]=prefix[i-1]+stones[i-1];
        }
        return solve(prefix,2,0);
    }
};