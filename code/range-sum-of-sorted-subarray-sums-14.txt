class Solution {
public:
    int rangeSum(vector<int>& a, int n, int l, int r) {
        vector<int> v;
        for(int i=0; i<n; i++) {
           int temp=0;
           for(int j=i; j<n; j++) {
               temp += a[j];
               v.push_back(temp);
           }
        }
        sort(begin(v), end(v));
        unsigned long long res = 0;
        for(int i=l-1; i<r; i++) {
            res += v[i];
        }
        return res%1000000007;
    }
};