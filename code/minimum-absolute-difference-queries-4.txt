class Solution {
public:
    vector<int> minDifference(vector<int>& nums, vector<vector<int>>& queries) {
        vector<int> index[101];
        int i = 0;
        for(auto x : nums) {
            index[x].push_back(i++);
        }
        vector<int> ans(queries.size());
        int j = 0;
        for(auto &q : queries) {
            int l = q[0], r = q[1];
            int prev = -1;
            int d = INT_MAX;
            for(int i = 1; i <= 100; i ++) {
                if(index[i].size() == 0) continue;
                int idx = lower_bound(index[i].begin(), index[i].end(), l) - index[i].begin();
                int idx2 = upper_bound(index[i].begin(), index[i].end(), r) - index[i].begin();
                if(idx2 <= idx) continue;
                if(prev != -1) {
                    d = min(i - prev, d);
                }
                if(d == 1) break; //early break, no answer better than 1
                prev = i;
            }
            ans[j] = d == INT_MAX ? -1 : d;
            j++;
        }
        return ans;
    }
};