class Solution {
public:
    int maxEqualRowsAfterFlips(vector<vector<int>>& matrix) {
        int n = matrix.size(), m = matrix[0].size();
        map<string, int> nums;
        for(int i=0; i<n; i++) {
            string st, ts;
            for(int j=0; j<m; j++) {
                st.push_back(matrix[i][j] + '0');
                ts.push_back((1 ^ matrix[i][j]) + '0');
            }
            nums[st]++;
            nums[ts]++;
        }
        int ans = 0;
        for(auto x: nums) {
            ans = max({ans, x.second});
        }
        return ans;
    }
};