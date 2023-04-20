class Solution {
public:
    long long interchangeableRectangles(vector<vector<int>>& nums) 
    {
        long long count=0;
        map<double,int>mp;
        for(auto it:nums)
        {
            double val=double(it[0]*1.0/it[1]);
            if(mp.count(val))
            {
                count+=mp[val];
            }
            mp[val]++;
        }
        return count;
    }
};