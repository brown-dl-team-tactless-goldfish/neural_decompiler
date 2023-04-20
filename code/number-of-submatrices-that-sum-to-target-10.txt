class Solution {
public:
    int numSubmatrixSumTarget(vector<vector<int>>& matrix, int target) {
        //calculate the prefix sum
         for(int r = 0;r<matrix.size();r++)
         {
             for(int c = 1;c<matrix[0].size();c++)
             {
                 matrix[r][c] += matrix[r][c-1];
             }
         }
        //Here the magic begin
        int res = 0;
        for(int fixColumn = 0;fixColumn < matrix[0].size();fixColumn++)
        {
            for(int subMatrixCol = fixColumn;subMatrixCol < matrix[0].size();subMatrixCol++)
            {
                unordered_map<int,int>mp;
                mp[0] = 1;
                int sum = 0;//sum of current sub-matrix
                for(int currentRow = 0;currentRow<matrix.size();currentRow++)
                {
                    //when fixed point is 2nd col and onward, we have to subtract previous cols
                    if(fixColumn>0) matrix[currentRow][subMatrixCol] -=  matrix[currentRow][fixColumn-1];
                    sum+=(matrix[currentRow][subMatrixCol]); // calculating the sum w.r.t column
                    if(mp[sum-target]) res+=mp[sum-target];
                    mp[sum]++; // you can get this idea by solving, sub-array target problem
                }
            }
        }
        
        return res;
    }
};