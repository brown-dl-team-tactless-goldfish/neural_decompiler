class Solution {
public:
    int partitionDisjoint(vector<int>& A) {
        int l = A.size();
        vector<int> left(l-1, 0);
        vector<int> right(l, 0);
        right[l-1] = A.back();
        for (int i=l-2; i>=0; i--){
            right[i] = min(right[i+1], A[i]);
        }
        left[0] = A[0];
        if (left[0] <= right[1]) return 1;
        for (int i=1; i<l-1; i++){
            left[i] = max(left[i-1], A[i]);
            if (left[i] <= right[i+1]) return i+1;
        }
        return -1;
    }
};