// Please, UpVote, if you like it :-)
class Solution {
public:
    int beautySum(string s) {
        int res = 0;
        map<char, int> freq;
        for (int i = 0; i < s.size(); i++) {
            freq.clear();
            for (int j = i; j < s.size(); j++) {
                freq[s[j]]++;
                calculate(freq, res);
            }
        }
        return res;
    }
private:
    void calculate(map<char, int>& freq, int& res) {
        int minFreq = INT_MAX, maxFreq = INT_MIN;
        for (auto f : freq) {
            if (f.second < minFreq)
                minFreq = f.second;
            if (f.second > maxFreq)
                maxFreq = f.second;
        }
        res += (maxFreq - minFreq);
    }
};