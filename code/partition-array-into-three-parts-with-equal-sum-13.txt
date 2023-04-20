class Solution {
public:
    bool canThreePartsEqualSum(vector<int>& A) {
        int sum = 0;
        for (auto& t: A) sum += t;
        if (sum % 3 != 0) return false;
        sum /= 3;
        int sum1 = 0;
        int i1 = -1;
        int n = A.size();
        for (int i = 0; i < n; i++){
            sum1 += A[i];
            if (sum1 == sum) {
                i1 = i;
                break;
            }
        }
        if (i1 == -1) return false;
        
        int i3 = -1;
        int sum3 = 0;
        for (int i = n-1; i>= 0; i--){
            sum3 += A[i];
            if (sum3 == sum) {
                i3 = i;
                break;
            }
        }
        if (i3 == -1) return false;
        
        return (i3 > i1);
    }
};