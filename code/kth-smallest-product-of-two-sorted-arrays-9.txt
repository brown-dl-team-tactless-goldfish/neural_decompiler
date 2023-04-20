class Solution {
public:
    bool check(long long midval,vector<int>& nums1, vector<int>& nums2, long long k){
        long long cnt=0;
        for(int i=0;i<nums1.size();i++)
        {
            long long val=nums1[i];
			if(val==0 and midval>=0)
                cnt+=nums2.size();
            
            else if(val>0)
                cnt+=findmaxIndex(nums2,val,midval);
            
            else if(val<0)
                cnt+=findminIndex(nums2,val,midval);
        }
        return cnt>=k;
    }
    
    int findmaxIndex(vector<int>&nums2 , long long  val , long long midval)
    {
        int l = 0  , r = nums2.size()-1 , res=  -1;
        while(l<=r)
        {
            long long mid = (l+r)/2;
            if(val*nums2[mid]<=midval)
            {
                res=mid;
                l=mid+1;
            }
            else r=mid-1;
        }
        return res+1;
    }
    
    int findminIndex(vector<int>&nums2 , long long  val , long long midval)
    {
        int l = 0  , r = nums2.size()-1 , res=  r+1;
        while(l<=r)
        {
            long long mid = (l+r)/2;
            if(val*nums2[mid]<=midval)
            {
                res=mid;
                r=mid-1;
            }
            else l=mid+1;
        }
        return nums2.size()-res;
    }
    
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        long long l=-1e10,r=1e10,res=-1;
        while(l<=r){
            long long mid = (l+r)/2;
            if(check(mid,nums1,nums2,k)) {
                res=mid;
                r=mid-1;
            }
            else l=mid+1;
        }
        return res;
    }
};