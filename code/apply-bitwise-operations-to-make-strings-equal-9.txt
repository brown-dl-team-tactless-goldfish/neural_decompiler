class Solution {
public:
    bool makeStringsEqual(string s, string target) {
        if(s==target)
        {
            return true;
        }
        int n = target.size();
        int count=0, count0=0, count1=0;
        int count0T=0, count1T=0;
        for(int i =0;i<n;i++)
        {
            if(s[i]=='0')
            {
                count0++;
            }
            else
            {
                count1++;
            }
            if(target[i]=='0')
            {
                count0T++;
            }
            else
            {
                count1T++;
            }
            count++;
        }
        if(count==count0)
        {
            return false;
        }
        if(count0T==count)
        {
            return false;
        }
        return true;
    }
};