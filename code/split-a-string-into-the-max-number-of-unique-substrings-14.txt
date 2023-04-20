class Solution {
public:
    
    void dfs(string& s,unordered_set<string>& map, int& ans , int start){
        
        if(start == s.length()) {
            int ss = map.size();
            ans = max(ans,ss);
            return;
        }
        
        string curr = "";
        
        for(int i = start ; i< s.length();i++){
             curr +=s[i];
            if(map.find(curr) == map.end()){
                map.insert(curr);        
                dfs(s,map,ans,i+1);
                map.erase(curr);
            }
        }
    }
    
    int maxUniqueSplit(string s) {
        unordered_set<string> map;
        int ans = 0;
        dfs(s,map,ans,0);
        return ans;
        
    } 
};