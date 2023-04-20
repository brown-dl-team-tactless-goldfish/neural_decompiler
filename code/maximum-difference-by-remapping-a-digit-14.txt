class Solution 
{
public:
    int minMaxDifference(int num) 
    {
        string s = to_string(num);
        string t = s;
        int n=s.size();
        char digit;
        
        //making num maximum by replacing first non-nine digit with 9 
        for(int i=0; i<n; i++)
        {
            if(s[i] != '9') 
            {
                digit = s[i];
                s[i] = '9';
                while(i<n) //replacing all position of that digit with 9
                {
                    if(s[i]==digit)
                        s[i]='9';
                    i++;
                }
                break;
            }
        }
        int maxi = stoi(s);
        
        //making num minimum by replacing first non-zero digit with 0
        for(int i=0; i<n; i++)
        {
            if(t[i] != '0')
            {
                digit = t[i];
                t[i] = '0';
                while(i<n) //replacing all position of that digit with 0
                {
                    if(t[i]==digit)
                        t[i]='0';
                    i++;
                }
                break;
            }
        }
        int mini = stoi(t);
        return maxi-mini;
        
    }
};