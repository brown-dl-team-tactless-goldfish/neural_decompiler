bool isBoomerang(int** points, int pointsSize, int* pointsColSize){

	int y1 = points[1][1] - points[0][1];
	int x1 = points[1][0] - points[0][0];
	int y2 = points[2][1] - points[0][1];
	int x2 = points[2][0] - points[0][0];

	bool ret = true;

	if(y1 * x2 == x1 * y2) {
		ret = false;
	}

	return ret;
}