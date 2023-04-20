class Solution {
public:
    vector<vector<string>> mostPopularCreator(vector<string>& creators, vector<string>& ids, vector<int>& views) {
        //one map should hold creator and the views
        unordered_map<string,long long> map;
        //other map stores creator and {views and the id for the sorting sake}
        unordered_map<string,pair<int,string>> indmap;
        //we also hold max value to keep track of pewdiepie
        long long ma=INT_MIN;
        int n=views.size();
        for(int i=0;i<n;i++)
        {
            string c=creators[i];
            map[c]+=views[i];
            ma=max(ma,map[c]);
            if(indmap.find(c)==indmap.end())
            {
                indmap[c]={views[i],ids[i]};
            }else{
                if(indmap[c].first<views[i])
                {
                    indmap[c]={views[i],ids[i]};
                }else if(indmap[c].first==views[i] && indmap[c].second>ids[i])
                {
                    indmap[c]={views[i],ids[i]};
                }
            }
        }
        vector<vector<string>> ans;
        for(auto m: map){                         
            if(ma == m.second){
                ans.push_back({m.first, indmap[m.first].second});
            }
        }
        return ans;
    }
};