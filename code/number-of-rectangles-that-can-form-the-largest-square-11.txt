

int countGoodRectangles(int** rectangles, int rectanglesSize, int* rectanglesColSize)
{
    int rows=0;
    int columns=0;
    
    int count = 0;
    int max_side = 0;
    
    for(rows=0; rows<rectanglesSize; rows++)
    {
            int len = rectangles[rows][0];
            int wid = rectangles[rows][1];
        
            int side = (len>=wid ? wid : len);
            if(side > max_side)
            {
                count = 0;
                max_side = side;
            }
            
            if(side == max_side)
            {
                count++;
            }
    }
    return count;
}