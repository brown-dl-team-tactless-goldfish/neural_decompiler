class Solution {
public:
    vector<bool> checkArithmeticSubarrays(vector<int>& nums, vector<int>& l, vector<int>& r) {

        vector<bool> ans;
        int n = l.size();
        for(int i = 0 ; i < n; i++)
        {
            vector<int> level;
            for(int start = l[i]; start <= r[i]; start++)
            {
                level.push_back(nums[start]);
            }
            sort(level.begin(), level.end());
            if(level.size() == 1)
            {
                ans.push_back(true);
                continue;
            }
            int gap = level[1] - level[0];
            int c = 0;
            for(int x = 1; x < level.size(); x++)
            {
                if(level[x] - level[x - 1] != gap){
                    c = 1;
                    break;
                }
            }
            c == 1?ans.push_back(false) : ans.push_back(true);
        }
        return ans;
    }
};