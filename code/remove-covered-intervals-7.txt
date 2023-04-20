class Solution {
public:
    int removeCoveredIntervals(vector<vector<int>>& v) {
        
        
        sort( v.begin( ), v.end( ), [ ]( const auto& lhs, const auto& rhs )
            {
                if(lhs[0] == rhs[0]) return lhs[1] > rhs[1];
                return lhs[0] < rhs[0];
            });
        
        
        int n = v.size(), ans = 1, pos = 0;
        for(int i = 1; i<n; i++) {
            if(v[i][1] <= v[pos][1]) continue;
            ++ans;
            pos = i;
        }
        return ans;
    }
};