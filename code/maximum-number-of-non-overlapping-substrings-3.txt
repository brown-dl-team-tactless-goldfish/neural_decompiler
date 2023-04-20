class Solution {
public:
    vector<string> maxNumOfSubstrings(string s) {
        vector<int> l(26, INT_MAX);
        vector<int> r(26, INT_MIN);
        for (int i = 0; i < s.size(); i++) {
            l[s[i] - 'a'] = min(l[s[i] - 'a'], i);
            r[s[i] - 'a'] = max(r[s[i] - 'a'], i);
        }
        vector<string> res;
        int old_right = -1;
        for (int i = 0; i < s.size(); i++) {
            if (i != l[s[i] - 'a']) continue;
            int right = Check(i, l, r, s);
            if (right == -1) continue;
            if (right > old_right) res.push_back("");
            res.back() = s.substr(i, right - i + 1);
            old_right = right;
        }
        return res;
    }
    int Check(int i, vector<int>& l, vector<int>& r, string& s) {
        int right = r[s[i] - 'a'];
        for (int j = i + 1; j < right; j++) {
            if (l[s[j] - 'a'] < i) return -1;
            right = max(right, r[s[j] - 'a']);
        }
        return right;
    }
};