class Solution {
public:
    int countOrders(int n) {
        int M=1e9+7, ans=1;
        for(int i=2; i<=n; i++) {
            long long comb=(i*(2*i-1))%M;
            ans=(ans*comb)%M;
        }
        return ans;
    }
};