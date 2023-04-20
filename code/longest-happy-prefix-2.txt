class Solution {
public:
    string longestPrefix(string s) {
        int i = 1, j = 0, n = s.size();
        vector<int> ans(n, 0);
        while(i < n)
        {
            if(s[i] == s[j])
            {
                ans[i] = j+1;
                j++;
                i++;
            }
            else
            {
                if(j > 0)
                {
                    j = ans[j-1];
                }
                else
                {
                    ans[i] = 0;
                    i++;
                }
            }
        }
        int val = ans[n-1];
        return s.substr(0,val);
    }
};