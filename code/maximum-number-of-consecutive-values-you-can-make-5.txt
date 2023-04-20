class Solution {
public:
        int getMaximumConsecutive(vector<int>& A) {
        sort(A.begin(), A.end());
        int res = 1;
        for (int a: A) {
            if (a > res) break;
            res += a;
        }
        return res;
    }
};