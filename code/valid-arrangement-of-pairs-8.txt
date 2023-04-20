class Solution {
public:
    vector<vector<int>> validArrangement(vector<vector<int>>& p) {
    
        unordered_map<int,vector<int>>g;
        
        unordered_map<int,int>degree;
        
        for(auto it:p){
            g[it[0]].push_back(it[1]);
            degree[it[0]]++;
            degree[it[1]]--;
        }
        
        int start=p[0][0];
        for(auto it:degree){
            if(it.second==1){
                start=it.first;
                break;
            }
        }
        
        stack<int>st;
        st.push(start);
        vector<int>seq;
        
        while(st.size()>0){
            
            int x=st.top();
            
            while(g[x].size()>0){  // x->y->.....
                int y=g[x].back();
                g[x].pop_back();
                st.push(y);
                x=y;
            }
            
            int last=st.top();  // sequence end ho gya iss node par
            st.pop();
            seq.push_back(last);
            
        }
        
        reverse(seq.begin(),seq.end());
        
        int n=seq.size();
        
        vector<vector<int>>ans;
        
        for(int i=0;i<=n-2;i++){
            ans.push_back({seq[i],seq[i+1]});
        }
        
        
        return ans;
    }
    
};