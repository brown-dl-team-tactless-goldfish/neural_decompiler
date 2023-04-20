int totalMoney(int n){
    int i, sum = 0;
    
    for(i = 0; i < n; i++){
        sum += (i / 7) + i % 7 + 1;
    }
    
    return sum;
}