class Solution {
public:
    bool static comp2(pair<int,int> &a,pair<int,int> &b)
    {
        return a.first>b.first;
    }
    bool static comp(pair<int,int> &a,pair<int,int> &b)
    {
        return a.second<b.second;
    }
    vector<int> maxSubsequence(vector<int>& nums, int k) {
        vector< pair<int,int> > v(nums.size());
        for(int i=0;i<nums.size();i++)
        {
            v[i].first=nums[i];
            v[i].second=i;
        }
        sort(v.begin(),v.end(),comp2);
        vector< pair<int,int> > ans;
        int c=0;
        for(int i=0;i<nums.size();i++)
        {
            ans.push_back(v[i]);
            c++;
            if(c==k)
            break;
        }
        vector<int> res;
        sort(ans.begin(),ans.end(),comp);
        for(int i=0;i<ans.size();i++)
        {
            res.push_back(ans[i].first);
        }
        return res;
    }
};