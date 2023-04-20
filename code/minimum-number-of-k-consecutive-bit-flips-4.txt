class Solution {
public:
    int minKBitFlips(vector<int>& A, int K) {
        int flip = 0, ans = 0, n = A.size();
        vector<int> flipped(n, 0);
        
        for (int i = 0; i < n; i++) {
            if (i >= K) { //cancel the influnce of last window
                flip ^= flipped[i-K];
            }
            if (A[i] ^ flip == 0) { //if this bit need flip
                if (i + K > n) return -1;
                flipped[i] = 1;
                ans++;
                flip ^= 1; 
            }
        }
        return ans;
    }
};