class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int n=nums.size();
        int sum=0,count=0,ans=INT_MIN;
        for(int i=0;i<n;i++)
        {            
            sum+=nums[i];
            
            ans=max(ans,sum);
            if(sum<0)
            {
                sum=0;
            }
            
           
        }
        return ans;
    }
    int maximumsSplicedArray(vector<int>& nums1, vector<int>& nums2) {
        
        vector<int> v1=nums1;
        vector<int> v2=nums2;
        
        int n=nums1.size();
        
        int sum1=0,sum2=0;
        
        for(int i=0;i<n;i++)
        {
            sum1+=nums1[i];
            sum2+=nums2[i];
            
            nums2[i]-=nums1[i];
        }
        
        
        int res1=sum1+maxSubArray(nums2);
        
        
        nums2=v2;
        
        for(int i=0;i<n;i++)
        {
            nums1[i]-=nums2[i];
        }
        
        int res2=sum2+maxSubArray(nums1);
        
        return max(res1,res2);
        
        
        
        
    }
};