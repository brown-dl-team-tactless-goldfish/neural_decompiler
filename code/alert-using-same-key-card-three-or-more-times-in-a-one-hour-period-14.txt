class Solution {
public:
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        map<string,vector<int>> mpp ;
        for(int i = 0 ; i < keyName.size() ; ++i ){
            int mins =  stoi(keyTime[i].substr(0,2)) *60 + stoi(keyTime[i].substr(3)) ;
            mpp[keyName[i]].push_back(mins) ;
        }
        
        vector<string> ans ;
        for(auto &x : mpp){
            vector<int>&time = x.second ;
            sort(begin(time),end(time)) ;
            for(int e = 0 , s = 0 ; e < time.size() ; ++e){
                while(time[e]  - time[s] > 60 ) ++s ;
                if(e-s >= 2) {ans.push_back(x.first) ;break;}
            }
        }
        return ans ;
    }
};