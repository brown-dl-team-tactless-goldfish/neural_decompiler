class Solution {
public:
    string makeFancyString(string s) {
        int count = 0, i = 0;
        char prev = s[0];
        
        for (auto c : s) {
            
            if (c == prev) count++;
            
            else {
                count = 1;
                prev = c;
            }
            
            if (count < 3) s[i++] = c;
        }
        
        s.erase(i);
        return s;
    }
};