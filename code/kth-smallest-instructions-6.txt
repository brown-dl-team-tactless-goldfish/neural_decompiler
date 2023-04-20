class Solution {
 int comb(int n, int r) {
        long ans = 1;
        for (int i = 1, j = n - r + 1; i <= r; ++i, ++j) ans = ans * j / i;
        return ans;
    }
public:
    string kthSmallestPath(vector<int>& A, int k) {
        int h = A[1], v = A[0], N = h + v;
        string s;
        for (int i = 0; i < N; ++i) {
            if (h) { 
                int c = comb(h - 1 + v, v); 
                if (k <= c) { 
                    s += 'H';
                    --h;
                } else { 
                    k -= c;
                    s += 'V';
                    --v;
                }
            } else { 
                s += 'V';
                --v;
            }
        }
        return s;
    }
};