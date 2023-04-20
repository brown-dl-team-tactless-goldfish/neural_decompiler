class Solution {
public:
    vector<int> minInterval(vector<vector<int>>& intervals, vector<int>& queries) {
        sort(intervals.begin(), intervals.end(), [&](const vector<int> &x, const vector<int> &y) {
            return x[1] - x[0] < y[1] - y[0];
        });
        int i, n = queries.size();
        vector<int> ret(n, -1);
        set<pair<int, int>> st;
        for(i=0; i<n; i++)
            st.insert({queries[i], i});
        for(i=0; i<intervals.size(); i++) {
            int start = intervals[i][0], end = intervals[i][1];
            auto it = st.lower_bound({start, 0});
            while(it != st.end() && it->first <= end) {
                auto it2 = next(it);
                ret[it->second] = end - start + 1;
                st.erase(it);
                it = it2;
            }
        }
        return ret;
    }
};