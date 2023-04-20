class Solution {
public:
    vector<int> peopleIndexes(vector<vector<string>>& favoriteCompanies) {
        unordered_map<string, int> m;
        int id = 1, sz = favoriteCompanies.size();
		
        for (const auto &fc: favoriteCompanies) {
            for (const auto &c: fc) {
                if (m.count(c) > 0) continue;
                m[c] = id++;
            }
        }
		
        vector<bitset<50001>> vec;
        for (const auto &fc: favoriteCompanies) {
            bitset<50001> b;
            for (const auto &c: fc) {
                b[m[c]] = 1;
            }
            vec.push_back(b);
        }
		
        vector<int> res;
        for (int i = 0; i < sz; ++i) {
            bool flag = true;
            for (int j = 0; j < sz and flag; ++j) {
                if (i == j) continue;
                if ((vec[i] & vec[j]) == vec[i]) flag = false;
            }
            if (flag) res.push_back(i);
        }
		
        return res;
    }
};