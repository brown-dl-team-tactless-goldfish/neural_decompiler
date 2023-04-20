class Solution {
public:
    
    // contribution of each index?
    // dp1[i] be number of subarray starting at index i and have odd sum
    // dp2[i] be number of subarray starting at index i and have even sum
    
    const int mod = 1e9+7;
    
    int numOfSubarrays(vector<int>& arr) {
        int n = arr.size();
        int dp1[n];
        int dp2[n];
        for(int i=0;i<n;i++) {
            dp1[i] = 0;
            dp2[i] = 0;
        }
        dp1[n-1] = arr[n-1]%2;
        dp2[n-1] = 1 - arr[n-1]%2;
        for(int i=n-2;i>=0;i--){
            if(arr[i]%2==0){
                dp1[i] += (dp1[i+1]);
                dp1[i]%=mod;
                dp2[i] += dp2[i+1];
                dp2[i] +=1;
                dp2[i]%=mod;
            }
            else{
                dp1[i] += dp2[i+1];
                dp1[i] +=1;
                dp1[i]%=mod;
                dp2[i] += dp1[i+1];
                dp2[i]%=mod;
            }
        }
        int ans = 0;
        for(int i=0;i<n;i++){
            ans+=dp1[i];
            ans%=mod;
        }
        // for(int i=0;i<n;i++){
        // cout<<dp1[i]<<" "<<dp2[i]<<'\n';
        // }
        return ans;
    }
};