class Solution {
public:
    int nthUglyNumber(int n, int A, int B, int C) {
        int lo = 1, hi = 2 * (int) 1e9, mid, num;
        long ab, ac, bc, abc;
        long a = long(A); long b = long(B); long c = long(C);
        ab = a*b/__gcd(a, b);
        ac = a*c/__gcd(a, c);
        bc = b*c/__gcd(b, c);
        abc = a*bc/__gcd(a, bc);
        while (lo<hi){
            mid = lo + (hi - lo)/2;
            num = mid/a + mid/b + mid/c - mid/ab - mid/ac - mid/bc + mid/abc;
            if (num>=n){
                hi = mid;
            }else{
                lo = mid+1;
            }
        }
        return lo;
    }
};