class Solution {
public:
    bool pos(const int M, vector<int>& tasks, vector<int>& workers, int pills, int strength) {        
        multiset<int> W;
        for (int i = int(workers.size()) - 1; i >= int(workers.size()) - M; i--)
            W.insert(workers[i]);
        
        for (int i = M - 1; i >= 0; i--) {
            auto it = W.lower_bound(tasks[i]);
            if (it == W.end()) {
                if (pills == 0)
                    return false;
                it = W.lower_bound(tasks[i] - strength);
                if (it == W.end())
                    return false;
                pills--;
            }
            W.erase(it);
        }
        return true;        
    }
    
    int maxTaskAssign(vector<int>& tasks, vector<int>& workers, int pills, int strength) {
        sort(tasks.begin(), tasks.end());
        sort(workers.begin(), workers.end());
        int L = 0;
        int R = min(int(tasks.size()), int(workers.size()));
        int ans;
        while (L <= R) {
            int M = (L + R) / 2;
            if (pos(M, tasks, workers, pills, strength)) {
                ans = M;
                L = M + 1;                
            }
            else
                R = M - 1;
        }
        return ans;
    }
};