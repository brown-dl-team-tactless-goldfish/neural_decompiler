class Solution {
public:
    int aux(string s, char a, char b){
        bool foundb = false;
        int afreq = 0 , bfreq = 0, res = 0;
        for (auto c:s){
            if (c==a) afreq++;
            else if (b==c) bfreq++;
            if (bfreq || foundb){
                if (bfreq) res = max(res , afreq - bfreq);
                else res = max(res , afreq - 1);
            }
            if (afreq - bfreq<0) {
                foundb = true;
                afreq = bfreq = 0;
            }
        }
        return res;
    }
    int largestVariance(string s) {
        unordered_set<char> characters;
        for (auto i:s) characters.insert(i);
        int res = 0;
        for (auto a:characters){
            for (auto b:characters){
                if (a!=b) res = max(res , aux(s,a,b));
            }
        }
        return res;
    }
};