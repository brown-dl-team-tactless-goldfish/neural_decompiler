

int diagonalSum(int** mat, int matSize, int* matColSize)
{

    int rows = 0, columns = 0;
    int i=0;
    int prim_sum = 0;
    int sec_sum = 0;
    
    for(rows=0; rows<matSize; rows++)
    {
        prim_sum += mat[rows][i++];        
    }
    
    int excluded_num = 0;
    if(i%2 == 1)
    {
        excluded_num = mat[i/2][i/2];
        
    }
    
    for(rows=0; rows<matSize; rows++)
    {
        sec_sum += mat[rows][--i];
    }
    
    return (prim_sum + sec_sum - excluded_num);
    
}