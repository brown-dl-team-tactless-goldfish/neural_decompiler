#define ll long long
#define mod 1000000007
class Solution {
public:
    ll fact[100005];

    void factorial(ll n) {
        fact[0] = 1;
        for(ll i=1; i<=n; i++) fact[i] = i * fact[i-1] % mod;
    }

    ll powmod(ll a, ll b) {
        ll ans = 1;
        while(b > 0) {
            if(b & 1) ans = ans * a % mod;
            a = a * a % mod;
            b >>= 1;
        }
        return ans;
    }

    ll inv(ll x) {
        return powmod(x, mod-2);
    }
    
    int countAnagrams(string s) {
        ll n = s.size();
        factorial(n);
        s.push_back(' ');
        unordered_map<char, ll> mp;
        ll ans = 1, cnt = 0;
        for(auto c: s) {
            if(c == ' ') {
                ll up = fact[cnt];
                for(auto x: mp) {
                    ll down = fact[x.second];
                    up = up * inv(down) % mod;
                }
                ans = ans * up % mod;
                mp.clear();
                cnt = 0;
            }
            else {
                mp[c]++;
                cnt++;
            }
        }
        return ans;
    }
};