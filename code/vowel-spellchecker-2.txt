class Solution {
public:
    string removeVowels(string s) {
        for(int i = 0; i < s.size(); i++) {
            if(s[i] == 'a' || s[i] == 'e' || s[i] == 'o' || s[i] == 'u' || s[i] == 'i') s[i] = '*';
        }
        return s;
    }
    string tolow(string s) {
        string c;
        for(char x: s) c += tolower(x);
        return c;
    }
    vector<string> spellchecker(vector<string>& wordlist, vector<string>& queries) {
        unordered_map<string, string> c;
        unordered_map<string, string> v;
        unordered_set<string> s2;
        for(string word: wordlist) {
            s2.insert(word);
            string temp = tolow(word);
            if(c.find(temp) == c.end()) c[temp] = word;
            if(v.find(removeVowels(temp)) == v.end()) v[removeVowels(temp)] = word;
        }
        vector<string> ans;
        for(string q: queries) {
            string lq = tolow(q);
            if(s2.find(q) != s2.end()) ans.push_back(q);
            else if(c.find(lq) != c.end()) ans.push_back(c[lq]);
            else if(v.find(removeVowels(lq)) != v.end()) ans.push_back(v[removeVowels(lq)]);
            else ans.push_back("");
        }
        return ans;
    }
};