int* corpFlightBookings(int** bookings, int bookingsSize, int* bookingsColSize, int n, int* returnSize){
    int *res = (int*)malloc(sizeof(int)*(n+1));
    memset(res, 0, sizeof(int)*(n+1));
    * returnSize = n;
    for(int i=0; i<bookingsSize; i++){
        int start = bookings[i][0]-1;
        int end = bookings[i][1];
        int add = bookings[i][2];
        *(res+start) += add;
        *(res+end) -= add;
    }

    for (int j=1; j<n; j++){
        *(res+j) += *(res+j-1);
    }
    return res;
}