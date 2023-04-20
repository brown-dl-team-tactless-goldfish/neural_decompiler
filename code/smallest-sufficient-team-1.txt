// DP + Bit mask

class Solution {
public:
    vector<int> smallestSufficientTeam(vector<string>& skills, vector<vector<string>>& people) {
        int ns = skills.size(), np = people.size();
        
        // Issue indexes for each required skills
        unordered_map<string, int> m;
        for (string skill : skills)
            m[skill] = m.size();
        
        // Get bit mask for skills for each person
        vector<int> skillsMask;
        for (auto& person : people) {
            int mask = 0;
            for (string s : person) {
                mask |= (1 << m[s]);
            }
            skillsMask.push_back(mask);
        }
        
        // Dynamic programming
        vector<vector<int>> dp(np + 1, vector<int>(1 << ns, INT_MAX / 2));
        dp[0][0] = 0;
        vector<vector<int>> parent(np + 1, vector<int>(1 << ns, -1));

        for (int i = 0; i < np; i++) {
            int mask = skillsMask[i];
            for (int j = 0; j < 1 << ns; j++) {
                // Pick this person
                int nj = j | mask;
                if (dp[i][j] + 1 < dp[i + 1][nj]) {
                    dp[i + 1][nj] = dp[i][j] + 1;
                    parent[i + 1][nj] = j;
                }
                
                // Not pick this person
                if (dp[i][j] < dp[i + 1][j]) {
                    dp[i + 1][j] = dp[i][j];
                    parent[i + 1][j] = j;
                }
            }
        }
        
        // Backtracking
        vector<int> res;
        int r = np, c = (1 << ns) - 1;
        while (r > 0) {
            if (parent[r][c] != c) {
                res.push_back(r - 1);
                c = parent[r][c];
            }
            r--;
        }
        
        reverse(res.begin(), res.end());
        return res;
    }
};