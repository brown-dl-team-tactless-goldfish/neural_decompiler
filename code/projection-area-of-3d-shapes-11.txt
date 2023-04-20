

int projectionArea(int** grid, int gridSize, int* gridColSize)
{
    //Explaination
    //In xy coordinate- if a coordinate is present in grid, it will only take one unit (cube) of area
    //In yz coordinate- the larger height on same x coordinate will be reflected on the yz plane on same x coordinate
    //In zx coordinate- the larger hieght on same y cooridnate will be reflected on the xz plane on same y coordinate
    
    int i=0, j=0;
    int sum = 0;
    
    //Sum across XY Coordinate
    for(i=0; i<gridSize; i++)
    {
        for(j=0; j<*gridColSize; j++)
        {
            if(grid[i][j] > 0)
            {
                sum += 1;
            }
        }
    }

    
    //Sum across XZ Coordinate
    for(i=0; i<gridSize; i++)
    {
        int max = INT_MIN;
        for(j=0; j<*gridColSize; j++)
        {
            if(grid[i][j] >= max)
            {
                max = grid[i][j];
            }
        }
        sum += max;
    }
    
    //Sum across YZ Coordinate
    for(i=0; i<*gridColSize; i++)
    {
        int max = INT_MIN;
        for(j=0; j<gridSize; j++)
        {
            if(grid[j][i] >= max)
            {
                max = grid[j][i];
            }
        }
        sum += max;
    }
    return sum;
}