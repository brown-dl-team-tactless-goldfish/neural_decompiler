class Solution {
public:
    queue<int> q;
    vector<string> watchedVideosByFriends(vector<vector<string>>& watchedVideos, vector<vector<int>>& friends, int id, int level) 
    {
        vector<bool> visited(friends.size(),false);      //To track the visited `friends`
        unordered_map<string,int> count;        // Stores the frequency of all the  `watchedVideos` by a freind at required level
        vector<pair<int,string>> resultPairs;
        vector<string> result;
        q.push(id);                  //Push initial node/friend id.
        visited[id]=true;            
        while(!q.empty()&&level--)	{			//BFS to get to the level.
            for(int i=q.size();i;q.pop(),i--) {
                for(int &i:friends[q.front()])
                    if(!visited[i]) {
                        visited[i]=true;
                        q.push(i);
                    }
            }
        }
        while(!q.empty()) {                      //The queue at this moment will only have all the friends at required level
            for(string &s:watchedVideos[q.front()])
                count[s]++;
            q.pop();
        }
        for(auto it=count.begin();it!=count.end();it++) //Add results to the vector to sort by frequency first and then the string.
            resultPairs.push_back({it->second,it->first});
        sort(resultPairs.begin(),resultPairs.end());
        transform(resultPairs.begin(),resultPairs.end(),back_inserter(result),[](pair<int,string>&p){return p.second;}); //Transform the pairs to result
        return result;            
    }
};