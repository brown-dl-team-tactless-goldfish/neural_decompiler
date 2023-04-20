class Solution {
public:
    unordered_map<int, string> memo;
    
    string build(const vector<int>& cost, const int& target) {
        if (memo.count(target)) return memo[target];
        string s, t;
        for (int i = 0; i < 9; ++i)
            if (cost[i] <= target) {
                t = build(cost, target - cost[i]);
                if (t != "*") {
                    t = char('1' + i) + t;
                    s = s.length() < t.length() ? t : s.length() == t.length() && s < t ? t : s;
                }
            }
        return memo[target] = s.empty() ? "*" : s;
    }
    
    string largestNumber(vector<int>& cost, int target) {
        memo[0] = "";
        string ans = build(cost, target);
        return ans == "*" ? "0" : ans;
    }
};