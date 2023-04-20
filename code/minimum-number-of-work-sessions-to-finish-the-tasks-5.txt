class Solution {
public:
    vector<int> sessions;
    unordered_map<string , int> dp;
    
    string encodeState(int pos, vector<int>& sessions) {
        vector<int> copy = sessions;
        sort(copy.begin(), copy.end());
        
        string key = to_string(pos) + "$";
        for (int i = 0; i < copy.size(); i++)
            key += to_string(copy[i]) + "$";
        
        return key;
    }
    
    int solve(vector<int>& tasks, int n, int sessionTime, int pos) {
        if (pos >= n )
            return 0;
        
        string key = encodeState(pos, sessions);
        
        if (dp.find(key) != dp.end())
            return dp[key];
        
        sessions.push_back(tasks[pos]);
        int ans = 1 + solve(tasks, n, sessionTime, pos + 1);
        sessions.pop_back();
        
        for (int i = 0; i < sessions.size();i++) {
            if (sessions[i] + tasks[pos] <= sessionTime) {
                sessions[i] += tasks[pos];
                ans = min(ans, solve(tasks, n, sessionTime, pos + 1));
                sessions[i] -= tasks[pos];
            }
        }
        
        return dp[key] = ans;
    }
    
    int minSessions(vector<int>& tasks, int sessionTime) {
        int n = tasks.size();
        return solve(tasks, n, sessionTime, 0);
    }
};