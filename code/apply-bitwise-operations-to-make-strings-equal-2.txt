class Solution {
public:
    bool makeStringsEqual(string s, string t) {
        int n = s.size();
        unordered_map<char, int> m;
        for(char c : s) m[c]++;
        
        for(int i=0; i<n; i++) {
            if(s[i] != t[i] && s[i] == '0') {
                m['0']--;
                if(!m['0']) m.erase('0');
                if(m.find('1') == m.end()) return false;
                m['1']++;
            }
        }
        for(int i=0; i<n; i++) {
            if(s[i] != t[i] && s[i] == '1') {
                m['1']--;
                if(!m['1']) m.erase('1');
                if(m.find('1') == m.end()) return false;
                m['0']++;
            }
        }
        return true;
    }
};