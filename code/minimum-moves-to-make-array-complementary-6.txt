class Solution {
public:
    int minMoves(vector<int>& nums, int limit) {
        int n = nums.size();
       vector<int> v1(2*limit+2,0);
        for(int i=0;i<n/2;i++)
        {
            int mi = min(nums[i],nums[n-1-i]);
            int ma = max(nums[i],nums[n-1-i]);
            v1[0]+=2;
            v1[mi+1]+=-1;
            v1[mi+ma]+=-1;
            v1[mi+ma+1]+=1;
            v1[ma+limit+1]+=1;   
        }
        int ans= INT_MAX;
        for(int i=1;i<v1.size();i++)
        {    v1[i]+=v1[i-1];
            ans =min(ans,v1[i]);
        }
        return ans;   
        
    }
};