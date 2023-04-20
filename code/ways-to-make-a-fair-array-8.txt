class Solution {
public:
    int waysToMakeFair(vector<int>& nums) {
        int ans=0;
        int n=nums.size();
        vector<int> odd(n+1),even(n+1);
        for(int i=1;i<n+1;i++){
            if(i%2==0){
                odd[i]=nums[i-1]+odd[i-1];
                even[i]=even[i-1];
                
            }
            else{
                even[i]=nums[i-1]+even[i-1];
                odd[i]=odd[i-1];
            }
        }
        for(int i=1;i<=n;i++){
            if(odd[i-1]+odd[i]+even[n]==even[i-1]+even[i]+odd[n]){
                ans++;
            }
        }
        return ans;
    }
};