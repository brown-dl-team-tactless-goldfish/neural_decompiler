class Solution {
public:
    bool isRationalEqual(string s, string t) {
        
        auto fn = [&](string x) {
            auto i = x.find('('); 
            if (i != string::npos) {
                string rep = x.substr(i+1, x.size()-i-2); 
                x = x.substr(0, i); 
                for (int k = 17; k; --k) x += rep; 
            }
            return stod(x); 
        }; 
        
        return fn(s) == fn(t); 
    }
};