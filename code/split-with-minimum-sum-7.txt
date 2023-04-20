class Solution {
public:
    int splitNum(int num) {
        vector<int> v;
        while(num) v.push_back(num % 10), num /= 10;
        sort(v.begin(), v.end());
        int n = v.size(), ans = INT_MAX, i = 0, j = 1, a = 0, b = 0;
        
        for(int i=0; i<n; i += 2) a = a * 10 + v[i];
        for(int i=1; i<n; i += 2) b = b * 10 + v[i];
        return b + a;
    }
};