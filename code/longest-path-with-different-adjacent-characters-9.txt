class Solution {
public:
    vector<vector<int>> g;
    int ans=0;
    int dfs(int i,string& s){
        vector<int> a;
        for(auto nbr:g[i]){
            if(s[nbr]!=s[i]) a.push_back(1+dfs(nbr,s));
            else ans=max(ans,dfs(nbr,s));
        }
        sort(a.begin(),a.end(),greater<int>());
        if(a.size()>=2) ans=max(ans,a[0]+a[1]);
        if(a.size()==0) return 0;
        return a[0];
    }
    int longestPath(vector<int>& p, string s) {
        g=vector<vector<int>> (s.size());
        
        for(int i=1;i<p.size();i++){
             g[p[i]].push_back(i);
        }
        
        int val=dfs(0,s);
        ans=max(ans,val);
        return ans+1;
    }
};