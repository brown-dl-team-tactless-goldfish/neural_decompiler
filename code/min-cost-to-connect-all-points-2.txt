#define min(a, b) (a < b ? a : b)
int distance(int *a, int *b)
{
    return abs(a[0] - b[0]) + abs(a[1] - b[1]);
}

int minCostConnectPoints(int** points, int pointsSize, int* pointsColSize){
    int result = 0, current_point = 0; 
    int minCost[pointsSize];
    minCost[0] = 0;
    for(int i = 1; i < pointsSize; i++)
        minCost[i] = INT_MAX;
    bool *visited = (bool *)calloc(pointsSize, sizeof(bool));
    visited[0] = true;
	while (current_point >= 0) 
    {
		visited[current_point] = true;
		int minCurrent = INT_MAX;
		int next_point = -1;
		for(int point = 0; point < pointsSize; point++) 
        {
			if(visited[point] || point == current_point)
				continue;
			minCost[point] = min(distance(points[current_point], points[point]), minCost[point]);
			if(minCost[point] < minCurrent)
            { 
				minCurrent = minCost[point];
				next_point = point;
			}
		}
		result += ((minCurrent == INT_MAX) ? 0 : minCurrent);
		current_point = next_point;
	}
	return result;
}