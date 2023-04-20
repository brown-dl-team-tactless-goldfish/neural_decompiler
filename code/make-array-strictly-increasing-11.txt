class Solution {
public:
    
    int makeArrayIncreasing(vector<int>& arr1, vector<int>& arr2) {
        int n = arr1.size();
        
        vector<vector<int>> B(2, vector<int>(n+1, INT_MAX));
        std::sort(arr2.begin(), arr2.end());
        arr2.resize(std::unique(arr2.begin(), arr2.end()) - arr2.begin());
        
        B[0][0] = arr1[0];
        B[0][1] = arr2[0];
        int last = 1;
        for (int i=1; i<n; i++) {
            int this_last = -1;
            for (int j=last; j>=0; j--) {
                int &u = B[(i-1)%2][j];
                if (u == INT_MAX)
                    break;
                if (u < arr1[i]) {
                    B[i%2][j] = min(B[i%2][j], arr1[i]);
                    this_last = max(this_last, j);
                }
                auto it = upper_bound(arr2.begin(), arr2.end(), u);
                if (it != arr2.end()) {
                    int v = *it;
                    B[i%2][j+1] = min(B[i%2][j+1], v);
                    this_last = max(this_last, j+1);
                }
                u = INT_MAX;
            }
            last = this_last;
        }
        int ans = -1;
        for (int j=0; j<=n; j++) {
            if (B[(n-1)%2][j] != INT_MAX) {
                ans = j;
                break;
            }
        }
        return ans;
    }
};