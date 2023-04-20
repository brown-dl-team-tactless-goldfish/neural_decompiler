#define ll long long
class Solution {
public:
    ll poww(ll a, ll b, ll mod) {
        ll res = 1;
        
        while(b > 0) {
            if( b % 2 ) {
                res = (res * a) % mod;
            }
            a = (a * a) % mod;
            b >>= 1;
        }
        return res;
    }
    ll val(char c) {
        return c - 'a' + 1;
    }
    string subStrHash(string s, int power, int modulo, int k, int hashValue) {
        
        string original_s = s;
        ll mod = modulo, cur = 0, n = s.size(), l = 0, r = k - 1, min_l = n, pk1;
        
        reverse(s.begin(), s.end());
        for(int i = 0; i < k; ++i) {
            cur += val(s[i]) * poww( power, k - 1 - i, mod);
            cur %= mod;
        }
        if (cur == hashValue ) min_l = min(min_l, n - 1 - r) ;
        l++, r++;
        
        pk1 = poww(power, k - 1, mod);
        for(; r < n; ++l, ++r) {
            cur = ( cur + mod - (val(s[l - 1]) * pk1) % mod ) % mod;
            cur = ( (cur * power) % mod + val(s[r]) ) % mod;
            if (cur == hashValue ) min_l = min(min_l, n - 1 - r); 
        }   
        
        return original_s.substr(min_l, k);
        
    }
};