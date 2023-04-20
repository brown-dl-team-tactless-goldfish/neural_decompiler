class Solution {
public:
    vector<vector<int>> imageSmoother(vector<vector<int>>& M) {
        if(M.empty()) return vector<vector<int>>();
        vector<vector<int>> result(M.size(), vector<int>(M[0].size(),0));
        vector<pair<int,int>> dir({{-1,-1}, {0,-1}, {1,-1}, {-1,0}, {0,0}, {1,0}, {-1,1}, {0,1}, {1,1}});
        for(int i=0; i<M.size(); i++) {
            for(int j=0; j<M[0].size(); j++) {
                int nume = 0, deno = 0;
                for(const auto& d:dir) {
                    int ii = i+d.first, jj = j+d.second;
                    if(ii>=0 && ii<M.size() && jj>=0 && jj<M[0].size()) {
                        deno++;
                        nume+=M[ii][jj];
                    }
                }
                result[i][j]=nume/deno;
            }
        }
        return result;
    }
};