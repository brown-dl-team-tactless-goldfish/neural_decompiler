class Solution {
public:
    int minimumDeletions(vector<int>& nums) {
        int n = nums.size();
        if(n == 1) return 1;
        int mn = 0, mx = 0;
        for(int i = 1; i < n; i++)
        {
            if(nums[mn] > nums[i])
                mn = i;
            if(nums[mx] < nums[i])
                mx = i;
        }
        int a = min(mn,mx), b = max(mn,mx);
        return min({b+1,n-a,n+1+a-b});
    }
};