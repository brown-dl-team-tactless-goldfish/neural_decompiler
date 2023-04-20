class Solution {
public:
    int minimumLength(string s) {
        int left = 0, right = s.size()-1;
        while (left < right) {
            if (s[left] != s[right]) break;
            char c = s[left];
            while (left <= right && s[left]==c) ++left;
            while (left <= right && s[right]==c) --right;
        }
        return right+1-left;
    }
};