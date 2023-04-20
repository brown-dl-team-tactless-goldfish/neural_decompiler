class Solution {
public:
    long long makeSimilar(vector<int>& nums, vector<int>& target) {
        vector<long long> even1, even2, odd1, odd2;
        for(int i=0;i<nums.size();i++)
            nums[i]%2 ? odd1.push_back(nums[i]) : even1.push_back(nums[i]);
        for(int i=0;i<target.size();i++)
            target[i]%2 ? odd2.push_back(target[i]) : even2.push_back(target[i]);
        
        sort(even1.begin(),even1.end());
        sort(even2.begin(),even2.end());
        sort(odd1.begin(),odd1.end());
        sort(odd2.begin(),odd2.end());
        
        long long res = 0;
        for(int i=0;i<even1.size();i++)
            res += abs(even1[i]-even2[i]);
        for(int i=0;i<odd1.size();i++)
            res += abs(odd1[i]-odd2[i]);
        res/=4;
        
        return res;
    }
};