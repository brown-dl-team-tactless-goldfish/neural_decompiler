class Solution {
public:
    int longestSquareStreak(vector<int>& nums) {
        int ans = 0;
        sort(nums.begin(), nums.end());
        unordered_set<int> s;
        for(auto n: nums) s.insert(n);
        for(auto n: nums) {
            
            long long t = n;
            int c = 0;
            while(s.find(t) != s.end()){
                c++;
                s.erase(t);
                t = t*t;
            }
            ans = max(ans, c);
        }
        return ans<2?-1:ans;
    }
};