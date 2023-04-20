class Solution {
public:
    long long int cnt;
    long long get(vector<vector<int> > &ar, int i, int n){
        vector<int> vis(n,0);
        queue<vector<int> > q;
        
        vis[i] = 1;
        cnt++;
        
        q.push(ar[i]);
        while(!q.empty()){
            auto cur = q.front();
            q.pop();
            
            for(int j = 0; j < n; j++){
                if(!vis[j]){
                    long long int a = (ar[j][0] * 1ll - cur[0] * 1ll) * (ar[j][0] * 1ll - cur[0] * 1ll);    
                    long long int b = (ar[j][1] * 1ll - cur[1] * 1ll) * (ar[j][1] * 1ll - cur[1] * 1ll);
                    long long int c = cur[2] * 1ll * cur[2];
                    
                    // Check whether centre of new circle lies 
                    // on or inside the current circle
                    long long int k = a + b - c;
                    if(k <= 0){
                        vis[j] = 1;
                        q.push(ar[j]);
                        cnt++;
                    }
                }
            }
        }
        return cnt;
    }
    int maximumDetonation(vector<vector<int>>& ar) {
        int n = ar.size();
        long long int ans = -1;
        
        for(int i = 0; i < n; i++){
            cnt = 0;
            ans = max(ans, get(ar, i, n));
        }
        
        return ans;
    }
};