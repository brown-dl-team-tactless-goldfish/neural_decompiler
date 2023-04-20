class Solution {
public:
    bool makeEqual(vector<string>& words) {
        int len = words.size();
        if (len == 1) {
            return true;
        }
        unordered_map<char, int> map;
        for (string &word : words) {
            for (char c : word) {
                map[c]++;
            }
        }
        for (auto it : map) {
            if (it.second % len != 0) {
                return false;
            }
        }
        return true;
    }
};