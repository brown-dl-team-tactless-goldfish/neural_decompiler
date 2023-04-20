#define ll long long int
class Solution {
public:
    bool ispalin(int z)
    {
        string s=to_string(z);
        int i=0,j=s.length()-1;
        while(i<j)
        {
            if(s[i]!=s[j])
            {
                return false;
            }
            i++;
            j--;
        }
        return true;
    }
    bool sieve(int n)
    {
        if(n==1)
        return false;
        for(ll i=2;i*i<=n;i++)
        {
            if(n%i==0)
            return false;
        }
        return true;
    }
    int primePalindrome(int n) {
        if (99899*1e2 <= n && n <= 1e8)
        return 100030001;
        for(int j=n;j<1e8;j++)
        {
           if(sieve(j))
          {
               if(ispalin(j))
               {
                    return j;
               }
           }
        }
        return 0;
    }
};