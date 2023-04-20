class Solution {
public:
    long long dividePlayers(vector<int>& skills) 
    {
        int n = skills.size();
        sort(skills.begin(), skills.end());
        long long ans = (skills[0] * skills[n - 1]);
        int target = skills[0] + skills[n - 1];
        for (int i = 1, j = n - 2; i < j; i++, j--)
        {
            int sum = skills[i] + skills[j];
            if (sum != target) return -1;
            
            long long prod = skills[i] * skills[j];
            ans += prod;
        }
        return ans;
    }
};