int maxCount(int m, int n, int** ops, int opsSize, int* opsColSize){
    int res_l = m;
    int res_h = n;
    for(int i = 0; i < opsSize; i ++){
        if(ops[i][0] < res_l) res_l = ops[i][0];
        if(ops[i][1] < res_h) res_h = ops[i][1];
    }
    return res_l * res_h;
}