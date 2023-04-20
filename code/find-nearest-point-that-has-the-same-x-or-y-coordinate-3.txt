

int nearestValidPoint(int x, int y, int** points, int pointsSize, int* pointsColSize)
{
    int min_dist = INT_MAX;
    int min_index = -1;
    
    int rows = 0, cols = 0;
    for(rows=0; rows<pointsSize; rows++)
    {
        int x_dist = 0;
        int y_dist = 0;
        
        if(points[rows][0] == x )
        {
            y_dist = (y - points[rows][1]);
            if(y_dist < 0)
            {
                y_dist *= -1;
            }
            
            if(y_dist < min_dist)
            {
                min_dist = y_dist;
                min_index = rows;
            }
        }
        else if(points[rows][1] == y)
        {
            x_dist = (x - points[rows][0]);
            if(x_dist < 0)
            {
                x_dist *= -1;
            }
            
            if(x_dist < min_dist)
            {
                min_dist = x_dist;
                min_index = rows;
            }
        }
    }
    return min_index;
}