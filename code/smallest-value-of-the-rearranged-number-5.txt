class Solution {
    static bool comp(char &a, char &b)
    {
        return a >= b;
    }
public:
    long long smallestNumber(long long num) {
        if(num == 0) return num;
        if(num < 0)
        {
            string s = to_string(abs(num));
            sort(s.begin(), s.end(), comp);
            return -1*(long long)stol(s);
        }
        string s = to_string(num);
        sort(s.begin(), s.end());
        int i = 0;
        if(s[i] == '0')
        {
            while(s[i] == '0')
                i++;
            s[0] = s[i];
            s[i] = '0';
        }
        return (long long)stol(s);
    }
};