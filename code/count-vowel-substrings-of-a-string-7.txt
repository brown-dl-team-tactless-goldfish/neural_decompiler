class Solution
{
public:
    int count(string s)
    {
        int a = 0;
        map<char, int> mp;
        int st = 0;
        int n = s.length();
        for (int i = 0; i < n; i++)
        {
            mp[s[i]]++;

            while (mp['a'] > 0 && mp['e'] > 0 && mp['i'] > 0 && mp['o'] > 0 && mp['u'] > 0)
            {
                a += n - i;
                mp[s[st]]--;
                st += 1;
            }
        }
        return a;
    }
    int countVowelSubstrings(string word)
    {
        int k = 0;
        string t = "";
        for (char c : word)
        {
            if (c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u')
            {
                t += c;
            }
            else
            {
                if (t.length() > 0)
                {
                    k += count(t);
                }

                t = "";
            }
        }
        if (t.length() > 0)
        {
            k += count(t);
        }
        return k;
    }
};