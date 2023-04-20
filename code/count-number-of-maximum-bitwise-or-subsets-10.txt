class Solution {
public:
    int countMaxOrSubsets(vector<int>& nums) {
        int reach=0,res=0;
        for(auto x:nums){
            reach|=x;
        }
        auto Solve=[&](auto Solve,int ind,int val){
            if(val>67108864){
                return ;
            }
            if(val==reach){
                res++;
            }
            for(int i=ind;i<(int)nums.size();i++){
                Solve(Solve,i+1,val|nums[i]);
            }
        };
        Solve(Solve,0,0);
        return res;
    }
};