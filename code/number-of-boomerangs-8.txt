class Solution {
public:
    int numberOfBoomerangs(vector<vector<int>>& points) {
        int res = 0;
        for (int i = 0; i < points.size(); ++ i) {
            unordered_map<int,int> diffs;
            for (int j = 0; j < points.size(); ++ j) ++ diffs[pow(points[j][0] - points[i][0], 2) + pow(points[j][1] - points[i][1], 2)];
            for (const auto& p : diffs) res += (p.second - 1) * p.second;
        }
        return res;
    }
};