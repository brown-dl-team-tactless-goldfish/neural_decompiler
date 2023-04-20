class Solution
{
public:
    bool checkDistances(string s, vector<int> &distance)
    {
        int n = s.length();
        unordered_map<int, vector<int>> mp;
        for (int i = 0; i < n; i++)
        {
            mp[s[i]].push_back(i);
        }
        for (auto &x : mp)
        {
            int a = x.second[0];
            int b = x.second[1];
            int c = x.first - 'a';
            if (abs(b - a) != (distance[c] + 1))
                return false;
        }
        return true;
    }
};