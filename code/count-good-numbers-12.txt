#define ll long long
class Solution {
    public:
    ll bin_expo(ll a, ll b, ll p){
    a=a%p; if(a==0)return 0;
    ll res=1; while(b>0){
        if(b&1){
            res=(res*a)%p;} a=(a*a)%p;b=b>>1;}
         return res; 
}     
    int countGoodNumbers(long long n) {
        ll odd=n/2;
        ll even=n/2+ n%2;
        ll mod=1e9+7;
        ll res=bin_expo(5ll, even, mod)*bin_expo(4ll, odd, mod)%mod;
        return int(res);
    }
};