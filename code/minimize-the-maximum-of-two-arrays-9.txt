class Solution {
public:
    int minimizeSet(long long div1, long long div2, int cnt1, int cnt2)
    {
        long long lcm = (div1 * div2) / __gcd(div1, div2);
        long long total = cnt1 + cnt2;
        long long l = total, r = 1e12;
        long long ans = 0;
        while (l <= r)
        {
            long long mid = (l + r) / 2;
            long long both = mid / lcm;
            long long onlyA = mid / div2 - both;
            long long onlyB = mid / div1 - both;
            total = max(0ll, cnt1 - onlyA) + max(0ll, cnt2 - onlyB);
            if (mid - onlyA - onlyB >= total + both)
            {
                ans = mid;
                r = mid - 1;
            }
            else
                l = mid + 1;
        }
        return ans;
    }
};
/*Some Extra Test Cases:
78789 42659 58291 182389  => 240680
16 14 12 8                => 20
5 2 2 20                  => 39

*/