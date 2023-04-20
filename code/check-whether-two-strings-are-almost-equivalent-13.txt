class Solution
{
public:
    bool checkAlmostEquivalent(string word1, string word2)
    {
        int n1 = word1.size();
        int n2 = word2.size();
        unordered_map<char, int> mp1;
        unordered_map<char, int> mp2;
        for (auto x : word1)
        {
            mp1[x]++;
        }
        for (auto x : word2)
        {
            mp2[x]++;
        }
        for (auto x : mp1)
        {
            char c = x.first;
            if (mp2.find(c) == mp2.end() && mp1[c] > 3)
            {
                return false;
            }
            if (mp2.find(c) != mp2.end() && abs(mp1[c] - mp2[c]) > 3)
            {
                return false;
            }
        }
        for (auto x : mp2)
        {
            char c = x.first;
            if (mp1.find(c) == mp1.end() && mp2[c] > 3)
            {
                return false;
            }
            if (mp1.find(c) != mp1.end() && abs(mp1[c] - mp2[c]) > 3)
            {
                return false;
            }
        }
        return true;
    }
};