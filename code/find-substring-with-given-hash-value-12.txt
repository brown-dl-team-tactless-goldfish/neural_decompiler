class Solution {
public:
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        long long ans=0,curr=0,pk=1;
        int n=s.length(),res=0;
        for(int i=n-1;i>=0;i--)
        {
            curr=(curr*power+s[i]-'a'+1)%modulo;
            if(i+k>=n)
            {
                pk=power*pk%modulo;
            }
            else
            {
                curr=(curr-(s[i+k]-'a'+1)*pk%modulo+modulo)%modulo;
            }
            if(curr==hashValue)
            res=i;
        }
        return s.substr(res,k);
    }
};