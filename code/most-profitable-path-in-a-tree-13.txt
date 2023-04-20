class Solution {
public:
    bool computeArriveTimes(const vector<set<int>>& neighbors, int src, int dst, int depth, vector<bool>& visited, vector<int>& times) {
        visited[src] = true;

        bool found = false;
        if (src == dst) {
            times[src] = depth;
            found = true;
        }
        else {
            for (int neighbor : neighbors[src]) {
                if (!visited[neighbor]) {
                    found = computeArriveTimes(neighbors, neighbor, dst, depth + 1, visited, times);
                    if (found) {
                        times[src] = depth;
                        break;
                    }
                }
            }
        }

        visited[src] = false;
        return found;
    }

    void computePathIncome(const vector<set<int>>& neighbors, int node, int depth, vector<bool>& visited, vector<int>& times, vector<int>& amount, int income, int& ans) {
        visited[node] = true;

        if (depth < times[node]) {
            income += amount[node];
        }
        else if (depth == times[node]) {
            income += (amount[node] / 2);
        }

        bool isLeaf = true;
        for (int neighbor : neighbors[node]) {
            if (!visited[neighbor]) {
                isLeaf = false;
                computePathIncome(neighbors, neighbor, depth + 1, visited, times, amount, income, ans);
            }
        }

        if (isLeaf && ans < income) {
            ans = income;
        }

        visited[node] = false;
    }

    int mostProfitablePath(vector<vector<int>>& edges, int bob, vector<int>& amount) {
        size_t n = amount.size();

        vector<set<int>> neighbors(n);
        for (const auto& edge : edges) {
            neighbors[edge[0]].insert(edge[1]);
            neighbors[edge[1]].insert(edge[0]);
        }

        vector<bool> visited(n, false);

        vector<int> times(n, INT_MAX);
        computeArriveTimes(neighbors, bob, 0, 0, visited, times);

        int ans = INT_MIN;
        computePathIncome(neighbors, 0, 0, visited, times, amount, 0, ans);
        return ans;
    }
};
