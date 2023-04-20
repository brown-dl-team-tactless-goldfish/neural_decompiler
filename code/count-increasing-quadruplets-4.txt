class Solution {
public:
    long long countQuadruplets(vector<int>& nums) {
        int n=nums.size();
        vector<vector<int>> greaterThan(n,vector<int>(n,0)),lesserThan(n,vector<int>(n,0));
        // let greaterThan[i][j] represent number of elements in range i to j which are greater than nums[i]
        
        // let lesserThan[i][j] represent number of elements in range i to j which are lesser than nums[j];
        for(int i=0;i<n;i++){
            for(int j=i+1,greater=0;j<n;j++){
                greater+=(nums[j]>nums[i]);
                greaterThan[i][j]=greater;
            }
        }
        
        for(int i=0;i<n;i++){
            for(int j=i-1,smaller=0;j>=0;j--){
                smaller+=(nums[j]<nums[i]);
                lesserThan[j][i]=smaller;
            }
        }

        long long res=0;
        for(int j=1;j<n-2;j++){
            for(int k=j+1;k<n-1;k++){
                if(nums[j]>nums[k]){
                    int poss_i=(lesserThan[0][k]-lesserThan[j][k]);
                    int poss_l=(greaterThan[j][n-1]-greaterThan[j][k]);
                    res+=1ll*poss_i*poss_l;
                }
            }
        }
        return res;
        
    }
};