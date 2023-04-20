class Solution {
public:
    int longestSquareStreak(vector<int>& nums) 
    {
        map<long long,long long> mp;
        int n = nums.size();
        
        for(auto it : nums)
        {
            mp[it]++;
        }
        
        int mx = -1;
        bool flag = false;
        for(auto it : mp)
        {
            long long curr = it.first*it.first;
            int cnt = 1;
            while(mp.count(curr)==1)
            {
                cout<<curr<<" ";
                flag = true;
                cnt++;
                curr = curr*curr;
            }
            
            mx = max(cnt,mx);
        }
        
        if(!flag) return -1;
        
        return mx;
    }
};