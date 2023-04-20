class Solution
{
public:
    vector<string> possibleValues(string k)
    {
        vector<string> v;
        for (int i = 0; i < 4; i++)
        {
            int d = -1;
            while (d <= 1)
            {
                string s = k;
                char c = s[i];
                int k = c - '0';
                int k1 = (k + d + 10) % 10;
                s[i] = k1 + '0';
                v.push_back(s);
                d += 2;
            }
        }
        return v;
    }
    int openLock(vector<string> &deadends, string target)
    {
        set<string> st(deadends.begin(), deadends.end());
        int steps = 0;
        string start = "0000";
        if (st.count(start))
            return -1;
        queue<string> q;
        q.push(start);
        while (!q.empty())
        {
            int n = q.size();
            for (int i = 0; i < n; i++)
            {
                string s = q.front();
                if (s == target)
                    return steps;
                q.pop();
                vector<string> v = possibleValues(s);
                for (auto x : v)
                {
                    if (st.count(x))
                        continue;
                    st.insert(x);
                    q.push(x);
                }
            }
            steps++;
        }
        return -1;
    }
};