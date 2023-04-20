int* sortedSquares(int* A, int ASize, int* returnSize){
    int* arr = malloc(sizeof(int)*ASize);
    *returnSize = ASize;
    int end = ASize-1, start = 0, ptr = ASize-1;
    while ((start <= end) && (ptr>=0))
    {
        if (pow(A[end],2) >= pow(A[start],2))
        {
            arr[ptr] = pow(A[end--],2);
        }
        else
        {
            arr[ptr] = pow(A[start++],2);
        }
        ptr--;
    }
    return arr;
}