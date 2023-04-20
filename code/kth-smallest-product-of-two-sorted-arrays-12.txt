class Solution {
public:
    long long kthSmallestProduct(vector<int>& nums1, vector<int>& nums2, long long k) {
        
        auto fn = [&](double val) {
            long long ans = 0; 
            for (auto& x : nums1) {
                if (x < 0) ans += nums2.end() - lower_bound(nums2.begin(), nums2.end(), ceil(val/x)); 
                else if (x == 0) {
                    if (0 <= val) ans += nums2.size(); 
                } else ans += upper_bound(nums2.begin(), nums2.end(), floor(val/x)) - nums2.begin(); 
            }
            return ans; 
        }; 
        
        long long lo = -pow(10ll, 10), hi = pow(10ll, 10)+1;
        while (lo < hi) {
            long long mid = lo + (hi - lo)/2; 
            if (fn(mid) < k) lo = mid + 1; 
            else hi = mid; 
        }
        return lo; 
    }
};