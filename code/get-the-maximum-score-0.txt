class Solution {
public:
    map<int, int> mp1, mp2;
    int n, m;
    vector<int> nums1,nums2;
    
    long long int dp[100002][2];
    int mod =1e9+7;
    
    long long int solve(int i, int c){
        if(c==0 && i>=n) return 0;
        if(c==1 && i>=m) return 0;
        
        if(dp[i][c]!=-1) return dp[i][c];
        
        if(c){
            if(mp1[nums2[i]]){
                dp[i][c]=max(nums2[i]+solve(mp1[nums2[i]],c^1), nums2[i]+solve(i+1,c));
            }
            else {dp[i][c]=(long long int)nums2[i]+solve(i+1,c); }
        }
        
        else{
            if( mp2[nums1[i]]){
                dp[i][c]=max(nums1[i]+solve(mp2[nums1[i]],c^1), nums1[i]+solve(i+1,c));
            }
            else {dp[i][c]=(long long int)nums1[i]+solve(i+1,c);}
        }
        return dp[i][c];
    }
    
    int maxSum(vector<int>& nums1, vector<int>& nums2) {
        n=nums1.size();
        m=nums2.size();
        this->nums1 = nums1;
        this->nums2 = nums2;
        memset(dp,-1,sizeof dp);
        
        for(int i=0;i<n;i++){
            mp1[nums1[i]] = i+1;
        }
        for(int i=0;i<m;i++){
            mp2[nums2[i]]=i+1;
        }
        
        long long int ans=max(solve(0,0), solve(0,1));
        
        return ans%mod;
    }
};