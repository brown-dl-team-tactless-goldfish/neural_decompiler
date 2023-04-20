class Solution {
public:
    bool isTransformable(string s, string t) {
        int n = s.length();
        bool vis[n];
        memset(vis, 0, sizeof(vis));
        int j = 0;
        unordered_map<char, list<int>> data;
        for(int i=0; i<n; i++){
            data[s[i]].push_back(i);
        }
        while(j < n){
            if(data.count(t[j]) <= 0){
                return false;
            }
            int pos = data[t[j]].front();
            data[t[j]].pop_front();
            if(data[t[j]].size() <= 0){
                data.erase(t[j]);
            }
            char x = t[j];
            x--;
            while(x >= '0'){
                if(data.count(x) > 0 && data[x].front() < pos){
                    return false;
                }
                x--;
            }
            j++;
        }
        for(auto itr=data.begin(); itr!=data.end(); itr++){
            if(data[itr->first].size() > 0){
                return false;
            }
        }
        return true;
    }
};