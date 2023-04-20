class Solution {
public:
    long long countSubarrays(vector<int>& nums, int minK, int maxK) {
        int n=nums.size();
        vector<int>mn,mx;
        long long ans=0;
        for(int i=0;i<nums.size();i++){
            if(nums[i]==minK)mn.push_back(i);
            if(nums[i]==maxK)mx.push_back(i);
        }
        for(int i=0;i<n;i++){
            if(nums[i]<minK || nums[i]>maxK){
                continue;
            }
            long long l=i;
            while(i<n&& nums[i]>=minK&&nums[i]<=maxK){
                i++;
            }
            i--;
            long long last=l-1;
            for(int j=l;j<=i;j++){
                if(nums[j]==minK){
                    int next=lower_bound(mx.begin(),mx.end(),j)-mx.begin();
                    long long cnt1=j-last;
                    if(next==mx.size())continue;
                    long long cnt2=i-mx[next]+1;
                    if(cnt2>0) ans+=(cnt1*cnt2),last=j;
                }else if(nums[j]==maxK){
                    int next=lower_bound(mn.begin(),mn.end(),j)-mn.begin();
                    long long cnt1=j-last;
                    if(next==mn.size())continue;
                    long long cnt2=i-mn[next]+1;
                    if(cnt2>0)ans+=(cnt1*cnt2),last=j;
                }
            }
        }
        return ans;
    }
};