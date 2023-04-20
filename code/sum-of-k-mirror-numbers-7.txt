class Solution {
public:
    long long get_palin_num(long long num, bool odd) {
        long long x = num;
        if (odd) x /= 10;
        
        while (x) {
            num = num * 10 + x % 10;
            x /= 10;
        }
        return num;
    }
    
    string to_base(long long num, int &base) {
        string res = "";
        while (num) {
            res += num % base + '0';
            num /= base;
        }
        return res;
    }
    
    bool is_palin(long long &num, int &base) {
        string s = to_base(num, base);
        int lo = 0, hi = s.size() - 1;
        while (lo < hi) {
            if (s[lo++] != s[hi--]) return false;
        }
        return true;
    }
    
    long long kMirror(int k, int n) {
        long long sum = 0, num = 0;
        for (long long num_digit=1; n; num_digit*=10) {
            // odd number of digits
            for (long long cur=num_digit; n && cur < num_digit*10; ++cur) {
                num = get_palin_num(cur, true);
                if (is_palin(num, k)) {
                    sum += num;
                    --n;
                }
            }
            // even number of digits
            for (long long cur=num_digit; n && cur < num_digit*10; ++cur) {
                num = get_palin_num(cur, false);
                if (is_palin(num, k)) {
                    sum += num;
                    --n;
                }
            }
        }
        return sum;
    }
};