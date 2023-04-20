class Solution {
public:
    vector<int> avoidFlood(vector<int>& nums) 
    {
        int n=nums.size();
        vector<int>ans(n,-1);
        set<int>s;
        unordered_map<int,int>mp;
        for(int i=0;i<n;i++)
        {
            if(nums[i]==0)
            {
                s.insert(i);
                ans[i]=19;
            }
            else
            {
                if(mp.find(nums[i])!=mp.end())
                {
                    int index=mp[nums[i]];
                    auto it=s.lower_bound(index);
                    if(it==s.end())
                    {
                        return {};
                    }
                    ans[*it]=nums[i];
                    s.erase(it);
                }
                mp[nums[i]]=i;
            }
        }
        return ans;
    }
};