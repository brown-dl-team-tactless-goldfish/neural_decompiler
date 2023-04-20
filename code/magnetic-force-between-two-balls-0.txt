int cmpfunc(const void* a, const void* b){
    return *(int*)a - *(int*)b;
}

int countBall(int* position, int positionSize, int distance){
    int cn = 1;
    int ptr = position[0];
    for(int i = 1; i < positionSize; i++){
        if((position[i] - ptr) >= distance){
            ptr = position[i];
            cn++;
        }
    }
    return cn;
}

int maxDistance(int* position, int positionSize, int m){
    int i;
    
    qsort(position, positionSize, sizeof(int), cmpfunc);

    int left = 1, right = position[positionSize-1];
    int mid;
    while(left + 1 < right){
        mid = (left + right)/2;
        if(countBall(position, positionSize,mid) >= m)
            left = mid;
        else
            right = mid - 1;
    }
    
    if(countBall(position, positionSize, right) >= m)
        return right;
    else
        return left;    
}