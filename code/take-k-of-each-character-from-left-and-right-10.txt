class Solution {
public:
    int takeCharacters(string s, int k) {
        vector<int> freq(3, 0);
        for(auto c: s){
            freq[c - 'a']++;
        }
        for(int i = 0; i < 3; i++){ freq[i] -= k; if(freq[i] < 0) return -1; }
        int l = 0, r = 0;
        vector<int> curr(3, 0);
        int len = 0;
        while(r < s.size()){
            curr[s[r] - 'a']++;
            while(curr[s[r] - 'a'] > freq[s[r] - 'a']){
                curr[s[l] - 'a']--;
                l++;
            }
            len = max(len, r - l + 1);
            r++;
        }
        return s.size() - len;
    }
};