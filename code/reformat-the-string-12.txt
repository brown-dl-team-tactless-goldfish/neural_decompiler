class Solution {
public:
    string reformat(string s) {
        int c1(0), c2(0), i(0), j(0);
        
        for (const char& c: s)
            isalpha(c) ? c1++ : c2++;
        
        if (abs(c1 - c2) > 1) return "";
        
        string ans;
        
        while (ans.length() < s.length())
            if ((ans.length() % 2) ^ (c1 > c2)) {
                while (isdigit(s[i])) i++;
                ans += s[i++];
            } else {
                while (isalpha(s[j])) j++;
                ans += s[j++];
            }
        
        return ans;
    }
};