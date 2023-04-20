int cmp(const void *a, const void *b)
{
    const int  x = ((int **)a)[0][1];
    const int  y = ((int **)b)[0][1];
    if(x > y)
        return 1;
    else if(x < y)
        return -1;
    return 0;
}

int findMinArrowShots(int** points, int pointsSize, int* pointsColSize){
    qsort(points, pointsSize, sizeof(int *), cmp);
    int result = 1, min = points[0][1];
    for(int i = 1; i < pointsSize; i++)
    {
        if(points[i][0] > min)
        {
            result++;
            min = points[i][1];
        }
        else
            min = min < points[i][1] ? min : points[i][1];
    }
    return result;
}