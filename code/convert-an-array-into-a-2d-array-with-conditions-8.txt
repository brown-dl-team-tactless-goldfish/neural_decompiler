class Solution {
public:
    vector<vector<int>> findMatrix(vector<int>& nums) {
        unordered_map<int,int> mp;
        int mx=0, ans =0;
        for(auto i:nums)mp[i]++;
        for(auto i:mp){
            mx = max(mx, i.second);
        }
        
        vector<vector<int>> vec(mx);
        
        int c =0;
        while(true){
            for(auto &j:mp){
                if(j.second > 0){
                    mp[j.first]--;
                    vec[c].push_back(j.first);
                }
            }
            c++;
            if(c == mx)break;
        }
        return vec;
        
    }
};