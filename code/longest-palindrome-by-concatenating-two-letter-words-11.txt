class Solution {
public:
    int longestPalindrome(vector<string>& words) {
        unordered_map<string, int> mp;
        for(auto x: words) mp[x]++;
        int ans = 0, fl = 0;
        for(auto x: words) {
            if(x[0] == x[1]) {
                if(mp[x] % 2) {
                    fl = 1;
                    ans += 2 * (mp[x] - 1);
                    mp[x] = 0;
                }
                else {
                    ans += 2 * mp[x];
                    mp[x] = 0;
                }
            }
        }
        if(fl) ans += 2;
        for(auto x: words) {
            auto y = x;
            reverse(y.begin(), y.end());
            if(mp[x] > 0 and mp[y] > 0) {
                ans += 4;
                mp[x]--;
                mp[y]--;
            }
        }
        return ans;
    }
};