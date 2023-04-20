int numSquares(int n){
    int * temp = (int *)malloc((n+1)*sizeof(int));
    memset(temp, 10000, (n+1)*sizeof(int));
    temp[0] = 0;
    for(int i=1; i<=n; i++)
        for(int j=1; j*j<=i; j++)
            temp[i] = temp[i] < temp[i-j*j] + 1 ? temp[i] : temp[i-j*j] + 1;
    return temp[n];
}