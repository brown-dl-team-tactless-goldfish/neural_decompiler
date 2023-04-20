class Solution {
public:
    vector<vector<int>> dp;
    vector<vector<int>> tmp;
    int add(int a, int b) {
        if (a == INT_MAX || b == INT_MAX) return INT_MAX;
        return a + b;
    }
    int minCost(vector<int>& houses, vector<vector<int>>& cost, int n, int m, int target) {
        dp = vector<vector<int>>(target + 1, vector<int>(m + 1, INT_MAX));
        tmp = vector<vector<int>>(target + 1, vector<int>(m + 1, INT_MAX));
        
        for (int x = 1; x <= m; x++) {
            if (houses[0] == 0) {
                dp[1][x] = cost[0][x - 1];
            } else {
                dp[1][houses[0]] = 0;
            }
        } 
        for (int i = 1; i < houses.size(); i++) {
            int c = houses[i];
            
            for (int t = 1; t <= target; t++) {
                int a = INT_MAX;
                int b = INT_MAX;
                auto& d  = dp[t];
                for (int x = 1; x <= m; x++) {
                    if (d[x] < a) {
                        b = a;
                        a = d[x];
                    } else if (d[x] < b) {
                        b = d[x];
                    }
                }
                if (c != 0) {
                    tmp[t][c] = min(dp[t][c], tmp[t][c]);
                    if (t < target) {
                        tmp[t + 1][c] = add((dp[t][c] == a ? b : a) , 0);
                    }
                } else {
                    for (int x = 1; x <= m; x++) {
                        tmp[t][x] = min(add(dp[t][x] , cost[i][x - 1]), tmp[t][x]);
                        if (t < target) {
                            tmp[t + 1][x] = add((dp[t][x] == a ? b : a) , cost[i][x - 1]);
                        }
                    }
                }
            }
            
            swap(dp, tmp);
            for (int t = 1; t <= target; t++) {
                for (int x = 1; x <= m; x++) {
                    tmp[t][x] = INT_MAX;
                }
            }
        }
        int ans = INT_MAX;
        for (int x = 1; x <= m; x++) {
            ans = min(ans, dp[target][x]);
        }
        if (ans == INT_MAX) return -1;
        return ans;
    }
};