class Solution {
public:
    int mx = 0;
    int row = 0;
    int col = 0;
    unordered_set<int> v;
    Solution(int n_rows, int n_cols) {
        mx = n_rows * n_cols;
        row = n_rows;
        col = n_cols;
    }
    
    vector<int> flip() {
        if(v.size() == mx) return {};
        int r = rand() % mx;
        while(v.count(r)) {
            r = (++r) %mx;
        }
        v.insert(r);
        return {r / col, r % col };
    }
    
    void reset() {
        v = {};
    }
};