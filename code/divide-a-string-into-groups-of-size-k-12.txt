class Solution {
public:
    vector<string> divideString(string s, int k, char fill) {
        int n = s.length();
        vector<string> v1;
        
        for(int i=0;i<n;i+=k){
            v1.emplace_back(s.substr(i,k));
        }
        int m = v1.size();
        
        int l1 = k - v1[m-1].length();
        
        if(v1[m-1].length()!=k){
            while(l1--){
                v1[m-1]+=fill;
            }
        }
        return v1;
    }
};