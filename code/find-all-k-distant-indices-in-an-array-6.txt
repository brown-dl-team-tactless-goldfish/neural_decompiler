class Solution {
public:
    vector<int> findKDistantIndices(vector<int>& nums, int key, int k) {
        vector<int> ans;
        int n=nums.size(),start,finish;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==key)
            {
                start=max(0,i-k);
                finish=min(n-1,i+k);
                if(ans.size()!=0)
                {
                    start=max(start,ans[ans.size()-1]+1);
                }
                for(int i=start;i<=finish;i++)
                {
                    ans.push_back(i);
                }
            }
        }
        return ans;
    }
};