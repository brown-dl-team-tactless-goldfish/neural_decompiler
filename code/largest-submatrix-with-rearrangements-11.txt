class Solution {
public:
    int largestSubmatrix(vector<vector<int>>& matrix) {
        
        //for every column keep a track of number of consecutive ones upto the index
        int m=matrix.size();
        int n=matrix[0].size();
        for(int j=0;j<n;j++)
        {
            for(int i=0;i<m;i++)
            {
                if(matrix[i][j]==1)
                {
                    matrix[i][j]+=(i > 0 ) ? matrix[i-1][j] : 0;
                }
            }
        }
        
        //now for every row sort the values in reverse order(non increasing order)
        int res=INT_MIN;
        for(int i=0;i<m;i++)
        {
            sort(matrix[i].rbegin(),matrix[i].rend());
            
            //the problem can be now assumed as to find the  maximum rectangle  area from the histogram
            int currRes=INT_MIN;
            for(int j=0;j<n;j++)
            {
                currRes=max(currRes,matrix[i][j] * (j+1));
            }
            res=max(res,currRes);
            
        }
        return res;
    }
};