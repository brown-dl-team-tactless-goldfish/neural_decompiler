class Solution {
public:
    bool canBeValid(string s, string locked) {
        int n = s.size();
        if(n&1)
            return false;
        int lftbrak = 0, rhtbrak = 0;
        for(int i = 0; i < n; i++)
        {
            if(locked[i] == '1')
            {
                if(s[i] == ')')
                    lftbrak--;
                else
                    lftbrak++;
            }
            else
                lftbrak++;
            if(lftbrak < 0)
                return false;
        }
        for(int i = n-1; i >= 0; i--)
        {
            if(locked[i] == '1')
            {
                if(s[i] == '(')
                    rhtbrak--;
                else
                    rhtbrak++;
            }
            else
                rhtbrak++;
            if(rhtbrak < 0)
                return false;
        }
        return true;
    }
};