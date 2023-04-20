struct Trie
{
    Trie *ch[26] = {};
    int count = 0;
    void insert(string &s)
    {
        auto n = this;
        for (char c : s)
        {
            if (n->ch[c - 'a'] == nullptr)
            {
                n->ch[c - 'a'] = new Trie();
            }
            n = n->ch[c - 'a'];
            n->count++;
        }
    }
    int calc(string &s)
    {
        auto n = this;
        int ans = 0;
        for (char c : s)
        {
            if (n->ch[c - 'a'] != nullptr)
                ans += n->ch[c - 'a']->count;
            n = n->ch[c - 'a'];
        }
        return ans;
    }
};
class Solution
{
public:
    vector<int> sumPrefixScores(vector<string> &words)
    {
        Trie t;
        for (auto &x : words)
            t.insert(x);
        vector<int> res;
        for (auto &x : words)
            res.push_back(t.calc(x));
        return res;
    }
};