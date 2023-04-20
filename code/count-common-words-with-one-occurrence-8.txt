class Solution {
public:
    int countWords(vector<string>& words1, vector<string>& words2) {
        
    unordered_map<string, int> m1;
    unordered_map<string, int> m2;
    for (auto e : words1)
        m1[e]++;
    for (auto e : words2)
        m2[e]++;

    int count = 0;
    for (auto e : words1)
        if (m1[e]==1 && m2[e]==1)
            ++count;
    return count;

    }
};