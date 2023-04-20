class Solution {
public:
    int findMaxLength(vector<int>& nums) {
        unordered_map<int,int> mp; //map of <gain,index> form
        mp[0]=-1; //add starting index with default gain of 0 at -1
        //change all zeros to -1
        for(int i=0;i<nums.size();i++){
            nums[i]==0?nums[i]=-1:nums[i]=1;
        }
        int sum=0,res=0;
        for(int i=0;i<nums.size();i++){
            //cumulative sum
            sum+=nums[i];
            
            //check if value already exists in the map
            if(mp.find(sum)!=mp.end()){
                //finding the length of possible subarray and comparing with the max result
                res=max(res,i-mp[sum]);
            }
            else{
                //adding value to our map
                mp[sum]=i;
            }
        }
        return res;
    }
};