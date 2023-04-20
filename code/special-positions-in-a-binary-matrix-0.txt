

int numSpecial(int** mat, int matSize, int* matColSize)
{
    int count = 0;
    
    int rows=0, columns=0;
    int i=0;
    for(rows=0; rows<matSize; rows++)
    {
        for(columns=0; columns<*matColSize; columns++)
        {
            if(mat[rows][columns] == 1)
            {
                bool match = true;
                for(i=0; i<*matColSize; i++)
                {
                    if(mat[rows][i] == 1 && i!=columns)
                    {
                        match = false;
                        break;
                    }
                }
                
                if(!match)
                    break;
 
                for(i=0; i<matSize; i++)
                {
                    if(mat[i][columns] == 1 && i!=rows)
                    {
                            match = false;
                            break;
                        
                    }
                }
                
                if(match)
                    count++;
            }
        }
    }
    return count;
}