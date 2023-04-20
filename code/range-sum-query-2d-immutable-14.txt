public class NumMatrix 
{
    int[,] sum;
    public NumMatrix(int[][] matrix) 
    {
        if(matrix.Length == 0) return;
        int r = matrix.Length, c = matrix[0].Length;
        sum = new int[r + 1, c + 1];
        for(int i = 0; i < r; i++)
            for(int j = 0; j < c; j++)
                sum[i + 1, j + 1] =  sum[i + 1, j] + sum[i, j + 1] - sum[i, j] + matrix[i][j];
    }
    
    public int SumRegion(int row1, int col1, int row2, int col2) 
    {
        return sum[row2 + 1, col2 + 1] + sum[row1, col1] - sum[row1, col2 + 1] - sum[row2 + 1, col1];
    }
}