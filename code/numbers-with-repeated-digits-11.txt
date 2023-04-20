class Solution {
public:
    int numDupDigitsAtMostN(int n) {
        vector<int> digits;
        for (int x = n + 1; x > 0; x /= 10) {
            digits.push_back(x % 10);
        }
        reverse(digits.begin(), digits.end());
        int ans = 0, k = digits.size();
        for (int i = 1; i < k; ++i) {
            ans += 9 * A(9, i - 1);
        }
        set<int> seen;
        for (int i = 0; i < k; ++i) {
            for (int j = i > 0 ? 0 : 1; j < digits[i]; ++j) {
                if (!seen.count(j)) {
                    ans += A(9 - i, k - i - 1);
                }
            }
            if (seen.count(digits[i])) {
                break;
            }
            seen.insert(digits[i]);
        }
        return n - ans;
    }
    int A(int m, int n) {
        return n == 0 ? 1 : A(m, n - 1) * (m - n + 1);
    }
};