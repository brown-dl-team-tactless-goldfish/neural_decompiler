class Solution {
public:
    string orderlyQueue(string s, int k) {
        // if k == 1 then we rotate the string and find the lexicographically minimum string
        if(k == 1)
        {
            string ans = s;
            int n = s.length();
            for(int i = 0 ; i < n;i++)
            {
                // extracting end char and adding it to the front
                char c = s[n - 1];
                s.pop_back();
                s = c + s;
                // minimum of existing string and new string formed
                ans = min(s, ans);   
            }
            return ans;
        }
        // if k > 1 then we can rearrange the string anyway we like
        // so return the sorted string.
        sort(s.begin(), s.end());
        return s;
    }
};