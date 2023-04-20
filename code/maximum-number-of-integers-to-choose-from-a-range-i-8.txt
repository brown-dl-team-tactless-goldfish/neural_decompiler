class Solution {
public:
    int maxCount(vector<int>& banned, int n, int maxSum) {
        int ans = 0, sum = 0;
        unordered_set<int> Set(banned.begin(), banned.end()); 
        for(int i = 1; i <= n; i++) {
            if(Set.find(i) == Set.end()){
                sum += i;
                if(sum > maxSum) return ans;
                ans++;
            }
        }
        return ans;
    }
};