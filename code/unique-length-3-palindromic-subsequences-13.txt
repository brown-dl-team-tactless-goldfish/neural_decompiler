class Solution {
public:
    int countPalindromicSubsequence(string s) {
        unordered_map<char,pair<int,int>> map; // map char to (left , right)
        int res = 0;
        
        for(int i = 0 ; i < s.size() ; ++i)
        {
            if(map.find(s[i]) == map.end())
                map[s[i]] = make_pair(i , -1); 
            else
                map[s[i]].second = i;
        }
        for(auto p : map)
        {
            auto pair = p.second;
            if(pair.second != -1) // means current char occured 2 or more times
            {
                int left = pair.first , right = pair.second;
                unordered_set<int> uniques;
                for(int i = left + 1 ; i < right ; ++i)
                    uniques.insert(s[i]);
                res += uniques.size();
            }
        }
        return res;
    }
};