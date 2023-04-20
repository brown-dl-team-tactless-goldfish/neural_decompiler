class Solution {
public:
    vector<vector<int>> matrixRankTransform(vector<vector<int>>& matrix) {
        const int n = matrix.size(), m = matrix[0].size();
        vector<int> rowcolmax(n+m, 0);
        map<int, vector<pair<int,int>>> mp;
        for(int i=0;i<n;i++) for(int j=0;j<m;j++)
            mp[matrix[i][j]].push_back({i,j});
        auto vv = vector(n, vector(m, 0));
        for(const auto& [x, v] : mp){
            Union u;
            for(auto [i, j] : v) u.join(i, n+j);
            for(const auto& [_, group] : u.groups()){
                int val = 0;
                for(int i : group) val = max(val, rowcolmax[i]);
                for(int i : group) rowcolmax[i] = val+1;
            }
            for(auto [i, j] : v) vv[i][j] = rowcolmax[i];
        }
        return vv;
    }

    struct Union{
        unordered_map<int, vector<int>> groups(){
            unordered_map<int, vector<int>> res;
            for(auto [i, _] : mroot) res[root(i)].push_back(i);
            return res; 
        }

        int root(int i){
            if(mroot[i] == i) return i;
            return mroot[i] = root(mroot[i]);
        }

        void join(int i, int j){
            if(!mroot.count(i)) mroot[i] = i;
            if(!mroot.count(j)) mroot[j] = j;
            mroot[root(i)] = root(j);
        }

        unordered_map<int,int> mroot;
    };
};