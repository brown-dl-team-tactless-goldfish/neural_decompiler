class Solution 
{
public:
    long long dividePlayers(vector<int>& ss) 
    {
        int s = 2 * accumulate(ss.begin(), ss.end(), 0) / ss.size();
        long long chemistry = 0;
        
        unordered_map<long long, int> cnt;
        for (int n : ss) ++cnt[n];
        
        for (auto[v,c] : cnt)
            if (!cnt.count(s-v) || cnt[s-v] != c)
                return -1;
            else
                chemistry += c * v * (s-v);
        
        return chemistry / 2;
    }
};