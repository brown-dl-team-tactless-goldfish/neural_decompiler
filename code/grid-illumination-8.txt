class Solution {
    unordered_map<int, int> row, col, positiveDiag, negativeDiag;
    set<pair<int, int>> litLamps;
public:
    
    bool isLit(int i, int j){
        
        if(row[i] != 0 || col[j] != 0 || positiveDiag[i + j] != 0 || negativeDiag[i - j] != 0) return true;
        
        return false;
        
    }
    
    void switchOFF(int i, int j, int n){
        if(i < 0 || j < 0 || i >= n || j >= n) return;
        
        if(litLamps.find({i, j}) == litLamps.end()) return;
        
        litLamps.erase({i, j});
        
        row[i]--;
        col[j]--;
        positiveDiag[i + j]--;
        negativeDiag[i - j]--;
        
        return ;
    }
    
    vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
                
        int N = lamps.size(), M = queries.size();
        vector<int> ans(M, 0);
        
        for(int i = 0; i < N; i++){
            if(litLamps.find({lamps[i][0], lamps[i][1]}) != litLamps.end()) continue;            
            litLamps.insert({lamps[i][0], lamps[i][1]});
            row[lamps[i][0]]++;
            col[lamps[i][1]]++;
            positiveDiag[lamps[i][0] + lamps[i][1]]++;
            negativeDiag[lamps[i][0] - lamps[i][1]]++;
        }
        
        for(int i = 0; i < M; i++){
            
            int a = queries[i][0], b = queries[i][1];
            
            if(isLit(a, b)){
                ans[i] = 1;
            }
            
            switchOFF(a, b, n);
            switchOFF(a, b + 1, n);
            switchOFF(a + 1, b + 1, n);
            switchOFF(a + 1, b, n);
            switchOFF(a, b - 1, n);
            switchOFF(a - 1, b - 1, n);
            switchOFF(a - 1, b, n);
            switchOFF(a - 1, b + 1, n);
            switchOFF(a + 1, b - 1, n);
            
        }
        
        return ans;
        
    }
};