class Solution {
    int mod=1e9+7;
public:
    long long rec(int i,int j,vector<int>&nums1,vector<int>&nums2,vector<long long >&dp1,vector<long long>&dp2){
        // cout<<i<<j<<endl;
        if(i>=nums1.size()){
            return 0;
        }
        if(dp1[i]!=-1){
            return dp1[i];
        }
        long long  sum=0;
        while(j<nums2.size()&&nums2[j]<nums1[i]){
                j++;
        }
        if(j<nums2.size()&&nums1[i]==nums2[j]){
            sum+=(max(rec(i+1,j+1,nums1,nums2,dp1,dp2),rec(j+1,i+1,nums2,nums1,dp2,dp1))+(long long)nums1[i]);
        }
        else{
            sum+=(rec(i+1,j,nums1,nums2,dp1,dp2)+(long long)nums1[i]);
        }
        return dp1[i]=sum;
    }
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        vector<long long >dp1(nums1.size(),-1),dp2(nums2.size(),-1);
        int val= max(rec(0,0,nums1,nums2,dp1,dp2)%mod,rec(0,0,nums2,nums1,dp2,dp1)%mod);
        return val;
    }
};