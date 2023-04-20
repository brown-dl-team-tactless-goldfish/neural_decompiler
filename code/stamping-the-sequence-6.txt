class Solution {
    bool isExcepted(int i, string &s, string &stamp, int l)
    {
        int count = 0;
        for(int j = i; j < i+l; j++)
        {
            if(s[j] == '*')
                count++;
            else if(s[j] == stamp[j-i])
                continue;
            else
                return true;
        }
        if(count == l)
            return true;
        return false;
    }
public:
    vector<int> movesToStamp(string stamp, string target) {
        string s = target;
        int st = stamp.size(), tr = target.size();
        vector<int> ans;
        int star = 0, prev = 0;
        while(1)
        {
            for(int i = 0; i < tr-st+1; i++)
            {
                if(isExcepted(i, s, stamp, st))
                    continue;
                ans.push_back(i);
                for(int j = i; j < st+i; j++)
                {
                    if(s[j] == '*')
                        continue;
                    s[j] = '*';
                    star++;
                }
            }
            if(ans.size() > 10*tr || prev == star)
                break;
            prev = star;
            if(star == tr)
            {
                reverse(ans.begin(), ans.end());
                return ans;
            }
        }
        return {};
    }
};