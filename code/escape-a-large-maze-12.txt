class Solution {
    int n = 1e6;
    unordered_set<long long> wall;

    bool isValid(long long coor, unordered_set<long long>& seen) {
        long i = coor / n;
        long j = coor % n;

        if (seen.find(coor) != seen.end() || wall.find(coor) != wall.end()) return false;
        return true;
    }

    bool bfs(vector<int>& source, vector<int>& target) {
        unordered_set<long long> seen;
        queue<long long> q;
        q.push((long long)source[0] * n + source[1]);
        int processed = 0;
        while (!q.empty()) {
            long long curr = q.front();
            q.pop();

            if (!isValid(curr, seen)) continue;

            long i = curr / n;
            long j = curr % n;

            if (i == target[0] && j == target[1]) return true;

            if(i < n - 1)q.push((i + 1) * n + j);
            if(i > 0)q.push((i - 1) * n + j);
            if(j < n - 1)q.push(i * n + (j + 1));
            if(j > 0)q.push(i * n + (j - 1));

            seen.insert(curr);

            if (seen.size() == 20000) return true;
        }

        return false;
    }

public:
    bool isEscapePossible(vector<vector<int>>& blocked, vector<int>& source, vector<int>& target) {
        for (vector<int>& w : blocked) {
            wall.insert((long long)w[0] * n + w[1]);
        }

        return bfs(source, target) && bfs(target, source);
    }
};