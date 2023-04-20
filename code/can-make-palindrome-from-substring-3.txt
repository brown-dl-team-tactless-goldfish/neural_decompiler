class Solution {
public:
    vector<bool> canMakePaliQueries(string s, vector<vector<int>>& queries) {
        vector<bitset<26>> tmp = {bitset<26>()}; 
        
        vector<bool> res;
        
        for (const auto& c : s) {
            bitset<26> a = tmp.back(); 
            a[c - 'a'] = a[c - 'a'] ^ 1; 
            tmp.push_back(a);
        }
        
        for (const auto& query : queries) {
            bitset<26> cur = tmp[query[1] + 1] ^ tmp[query[0]];
            
            int count = cur.count();
            
            res.push_back(count / 2 <= query[2]);
        }                        
        
        return res;
    }
};
