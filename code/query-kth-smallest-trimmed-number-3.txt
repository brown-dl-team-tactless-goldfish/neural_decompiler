class Solution {
public:
    vector<int> smallestTrimmedNumbers(vector<string>& nums, vector<vector<int>>& queries) {
        vector<int> ans;
        for(auto q : queries){
            int k = q[0], t =  q[1];
            vector<pair<string,int>> str;
            int n = nums[0].size(), i = 0;
            for(auto &it : nums){
                if(n == t) str.push_back({it,i++});
                else str.push_back({it.substr(n-t),i++});
            }
            sort(str.begin(),str.end());
            ans.push_back(str[k-1].second);
        }
        return ans;
    }
};