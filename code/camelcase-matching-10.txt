class Solution {
public:
    bool check(string &a,string &b)
    {
        int i=0;
        for(char &c:b)
            if(isupper(c)&&a[i]!=c)            //We are only allowed to add lower case characters, Upper case must match with pattern
                return false;
            else if(c==a[i])                        //If pattern[i] matches c we move forward to find the next matching character from pattern
                i++;
        return i==a.length();                   //Return true only if all characters from patern are matched.
    }
    vector<bool> camelMatch(vector<string>& queries, string pattern) 
    {
        vector<bool> result;
        for(string &q:queries)
            result.push_back(check(pattern,q));
        return result;
    }
};