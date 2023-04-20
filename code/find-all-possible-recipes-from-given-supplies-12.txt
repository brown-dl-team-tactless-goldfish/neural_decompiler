class Solution {
public:
    unordered_map<string,vector<string>>dp;
    unordered_set<string>look;
    unordered_map<string,int>ind;
    vector<string> findAllRecipes(vector<string>& rec, vector<vector<string>>& ing, vector<string>& sup)
    {
        int j=0;
        for(auto it:sup)
        {
            look.insert(it);
        }
        for(auto it:rec)
        {
            ind[it]=0;
            for(auto &t:ing[j++])
            {
                if(look.find(t)==look.end())
                {
                    dp[t].push_back(it);
                    ind[it]++;
                }
            }
        }
        queue<string>q;
        for(auto it:ind)
        {
            if(it.second==0)
            {
                q.push(it.first);
            }
        }
        vector<string>ans;
        while(q.size())
        {
            auto temp=q.front();
            q.pop();
            ans.push_back(temp);
            for(auto &it:dp[temp])
            {
                if(--ind[it]==0)
                {
                    q.push(it);
                }
            }
        }
        return ans;
    }
};