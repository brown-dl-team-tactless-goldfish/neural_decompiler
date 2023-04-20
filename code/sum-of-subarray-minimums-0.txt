int sumSubarrayMins(int* arr, int arrSize){
    int *stk = calloc(arrSize, sizeof(int));
    int *PLE = calloc(arrSize, sizeof(int)); 
    // store the distance between element arr[i] and its PLE (Previous Less Element)
    int *NLE = calloc(arrSize, sizeof(int)); 
    // store the distance between element arr[i] and its NLE (Next Less Element)
    int pt = -1;    // current stack index, "-1" means the stack is empty

    //initialize
    for(int i = 0; i < arrSize; i++){
        PLE[i] = i + 1;
        NLE[i] = arrSize - i;
    } 

    for (int i = 0; i < arrSize; i++){
        while (pt != -1 && arr[stk[pt]] > arr[i]){
            int x = stk[pt];
            NLE[x] = i - x;
            pt--;       // pop
        } 
        PLE[i] = (pt == -1? i + 1: i - stk[pt]); 
        stk[++pt] = i;  // push the index to stack
    }
    free(stk);

    int sum = 0, mod = 1e9 + 7;
    for (int i = 0; i < arrSize; i++){
        sum = (sum + arr[i] * (unsigned)PLE[i] * (unsigned)NLE[i]) % mod;
    }
    free(PLE);
    free(NLE);
    return sum;
}