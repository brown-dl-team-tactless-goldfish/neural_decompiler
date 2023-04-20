class FindSumPairs {
public:
    unordered_map<int,int> ump;
    vector<int> temp1;
    vector<int> temp2;
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
       
        temp1=nums1;
        temp2=nums2;
        for(int i=0;i<temp2.size();i++){
            ump[temp2[i]]++;
        }  
    }
    
    void add(int index, int val) {
      ump[temp2[index]]--;
        temp2[index]+=val;
       ump[temp2[index]]++;
               
    }
    
    int count(int tot) {
   
        int cnt=0;
        for(int i=0;i<temp1.size();i++){
            if(ump.find(tot-temp1[i])!=ump.end()) cnt+=ump[tot-temp1[i]];
        }
        return cnt;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */