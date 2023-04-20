class Solution {
public:
    int maximumCostSubstring(string s, string chars, vector<int>& vals) {
        int m = chars.size(), sum = 0, ans = 0;
        vector<int> value(26);
        for(int i=0; i<26; i++) value[i] = i + 1;
        for(int i=0; i<m; i++) value[chars[i] - 'a'] = vals[i];
        
        for(char c : s) {
            sum += value[c - 'a'];
            ans = max(ans, sum);
            if(sum < 0) sum = 0; 
        }
        return ans;
    }
};