class Solution {
public:
    vector<vector<int>>dp;
    int fn(int ind,vector<int>&arr,int segment,int k) 
    {
        if(segment==0)
            return 0;
        if(ind>=arr.size())
            return 0;
        if(dp[ind][segment]!=-1)
            return dp[ind][segment];
        
        int non_pick=fn(ind+1,arr,segment,k); 
        int target=lower_bound(arr.begin(),arr.end(),arr[ind]+k+1)-arr.begin();
        int pick=target-ind; 
        
        pick+=fn(target,arr,segment-1,k);
        
        return dp[ind][segment]= max(non_pick,pick);
        
        
    }
        
    int maximizeWin(vector<int>& arr, int k) {
        int n=arr.size();
        dp.resize(n,vector<int>(3,-1));
        
        return fn(0,arr,2,k);
        
        
    }
};