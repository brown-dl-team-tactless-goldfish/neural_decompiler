class Solution 
{
public:
    int appendCharacters(string s, string t) 
    {
        int m=s.size(), n=t.size();
        int i=0, j=0; 
        
        while(i<m && j<n)
        {
            if(s[i]==t[j]) //if character of both strings match move both pointers
            {
                i++;
                j++;
            }
            else //if character doesn't match then move string s pointer only
                i++;
        }
        
        if((j==n)) return 0; //if we covered whole t string then no need to append character
        return n-j;
        
    }
};