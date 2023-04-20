class Solution {
public:
    int numMatchingSubseq(string S, vector<string>& words) {
        unordered_map<char, vector<int>> smap;
        int n = words.size();
        vector<int> pos(n);
        for (int i=0;i<n;i++) {
            smap[words[i][0]].push_back(i);
        }
        
        int count = 0;
        for (char c : S) {
            vector<int> v = smap[c];
            smap[c].clear();
            
            for (int idx : v) {
                pos[idx]++;
                if (pos[idx] == words[idx].size())
                    count++;
                else
                    smap[words[idx][pos[idx]]].push_back(idx);
            }
        }
        
        return count;
    }
};