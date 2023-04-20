class Solution {
public:
    vector<string> watchedVideosByFriends(vector<vector<string>>& videos, vector<vector<int>>& friends, int id, int level) {
        vector<int> dp(friends.size(),INT_MAX);
        int distance = 0;
        queue<int> q;
        q.push(id);
        unordered_map<string,int> count;
        while(q.size()){
            int size = q.size();
            for(int i = 0;i<size;i++){
                int x = q.front();
                q.pop();
                if(distance < dp[x]){
                    dp[x] = distance; 
                    if(dp[x] == level){
                        for(auto& v : videos[x]){
                            count[v]++;
                        }
                        continue;
                    }
                    for(int j : friends[x]){
                        q.push(j);
                    }
                }
            }
            distance++;
        }
        vector<pair<int,string>> tmp;
        for(auto& ptr : count){
            tmp.push_back({ptr.second,ptr.first});
        }
        sort(tmp.begin(),tmp.end(),[](auto& a, auto& b){
            if(a.first != b.first){
                return a.first < b.first;
            }
            return a.second < b.second;
        });
        vector<string> ret;
        for(auto& ptr : tmp){
            ret.push_back(ptr.second);
        }
        return ret;
    }
};