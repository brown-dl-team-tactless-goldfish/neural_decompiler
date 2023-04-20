class Solution {
public:
    int maxEqualFreq(vector<int> &nums) {
        unordered_map<int, int> p, q;
        int ans = 1;
        for (int i = 0; i < nums.size(); ++i) {
            int tmp = 0;
            if (p.find(nums[i]) != p.end())
                tmp = p[nums[i]];
            p[nums[i]]++;
            if (q.find(tmp) != q.end()) {
                if (q[tmp] == 1) q.erase(tmp);
                else if (q[tmp] > 1) q[tmp]--;
            }
            q[tmp + 1]++;
            if (q.size() == 2) {
                auto it = q.begin();
                int a = it->first, b = it->second;
                it++;
                int c = it->first, d = it->second;
                if (((a == 1 && b == 1) || (c == 1 && d == 1)) || ((a - c == 1 && b == 1) || (c - a == 1 && d == 1))) {
                    if (b == 1) ans = max(i + 1, ans);
                    if (d == 1) ans = max(i + 1, ans);
                }
            }
            if (q.size() == 1 && p.size() == i + 1) ans = max(i + 1, ans);
            if (p.size() == 1) ans = max(i + 1, ans);
        }
        return ans;
    }
};