class Solution {
public:
    int numSubmat(vector<vector<int>>& mat) {
        int r = mat.size();
        int c = mat[0].size();
        vector<int> rowDP(c, 0);
        int totalSum = 0;
        for(int i=0; i<r; i++){
            for(int j=0; j<c; j++){
                if(mat[i][j] > 0){
                    rowDP[j]++;
                    totalSum += rowDP[j]; //Column based increasing
                    int minUntilInRow = rowDP[j]; //Row based search
                    int k = j-1;
                    while(k >=0 && mat[i][k] > 0){
                        minUntilInRow = min(minUntilInRow, rowDP[k]);
                        totalSum += minUntilInRow;
                        k--;
                    }
                }
                else{
                    rowDP[j] = 0;
                }
            } 
        }
        return totalSum;
    }
};