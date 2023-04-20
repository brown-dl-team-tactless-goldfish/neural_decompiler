class Solution {
public:
    vector<int> maxDepthAfterSplit(string seq) {
        short curr = 0;
        vector<int> ret;
        for (char& c : seq)
        {
            if (c == '(')
            {
                ret.push_back(curr);
                curr ^= 1;
            }
            else
            {
                curr ^= 1;
                ret.push_back(curr);
            }
        }
        return ret;
    }
};