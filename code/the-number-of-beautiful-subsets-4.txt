class Solution {
public:
    int solve(vector<int>& nums,int index,int k,unordered_map<int,int>& s){
        if(index>=nums.size()){
            bool found=false;
            for(auto& x:s){
                if(x.second>0){
                    found=true;
                    break;
                }
            }
            if(found)
            return 1;
            return 0;
        }
        
        int include=0,notinclude=0;
        if(!s[nums[index]-k]){
            s[nums[index]]++;
            include=solve(nums,index+1,k,s);
            s[nums[index]]--;
        }
        
        notinclude= solve(nums,index+1,k,s);
        
        return include+notinclude;
    }
    
    int beautifulSubsets(vector<int>& nums, int k) {
        int index=0,prev=-1;
        sort(nums.begin(),nums.end());
        
        unordered_map<int,int> s;
        return solve(nums,index,k,s);
    }
};