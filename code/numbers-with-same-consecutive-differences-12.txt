class Solution {
private:
    vector<int> res;
public:
    void backtrack(vector<int>nums, int index, int &k, int ans)
    {
        if(index == nums.size())
        {
            res.push_back(ans);
            return;
        }
        
        for(int i = 0; i<=9; i++)
        {
            nums[index] = i;
            
            if(nums[0] != 0 and index > 0 and abs(nums[index] - nums[index -1]) == k)
            {
               backtrack(nums, index+1, k, ans*10 + nums[index]);
            }
            else if (index == 0)
            {
                backtrack(nums, index+1, k, i);
            }
        }
    }
    
    vector<int> numsSameConsecDiff(int n, int k) {
        vector<int>nums(n, 0);
        backtrack(nums, 0, k,0);
        return res;
    }
};