class Solution {
public:
    int minimizeTheDifference(vector<vector<int>>& mat, int target) {
        int baseSummary = 0;
        for (auto& vec : mat) {
            sort(vec.begin(), vec.end());
            vec.erase(unique(vec.begin(), vec.end()), vec.end());
            baseSummary += *vec.begin();
        }
        if (baseSummary >= target) {
            return baseSummary - target;
        }
        int minDifference = abs(baseSummary - target);
        std::set<int> rbt;
        rbt.insert(baseSummary);
        for (auto& vec : mat) {
            std::vector<int> more;
            for (auto v : vec) {
                if (v == *vec.begin()) {
                    continue;
                }
                for (auto p : rbt) {
                    if (p > target) {
                        break;
                    }
                    if (rbt.count(p + v - *vec.begin()) == 0) {
                        more.push_back(p + v - *vec.begin());
                    }
                    if ((p + v - *vec.begin()) == target) {
                        return 0;
                    }
                    if ((p + v - *vec.begin()) > target) {
                        break;
                    }
                }
            }
            for (auto m : more) {
                rbt.insert(m);
            }
        }
        for (auto v : rbt) {
            if (abs(v - target) < minDifference) {
                minDifference = abs(v - target);
            }
        }
        rbt.clear();
        return minDifference;
    }
};