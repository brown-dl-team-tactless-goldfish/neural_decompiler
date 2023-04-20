class FindSumPairs {
public:
    FindSumPairs(const vector<int>& nums1, const vector<int>& nums2) {
        for(auto i:nums1) ++um1[i];
        for(auto i:nums2) ++um2[i];
        nums=nums2;
    }
    
    void add(int index, int val) {
        --um2[nums[index]];
        nums[index]+=val;
        ++um2[nums[index]];
    }
    
    int count(int tot) {
        int res=0,n;
        for(const auto& [val,count]:um1) {
            n=tot-val;
            if(um2.count(n)) res+=count*um2[n];
        }
        return res;
    }
private:
    vector<int> nums;
    unordered_map<int,int> um1,um2;
};