class Solution {
public:
   unordered_map<int,int> mp;
    
    vector<int> arrayChange(vector<int>& nums, vector<vector<int>>& operations) {
        for(int i=0 ; i < nums.size() ; i++) mp[nums[i]] = i; 
        for(vector<int> a : operations) mp[a[1]] = mp[a[0]] , mp[a[0]] = -1; 
        for(auto i : mp)
            if(i.second >= 0) 
                nums[i.second] = i.first;
        return nums;
    }
};