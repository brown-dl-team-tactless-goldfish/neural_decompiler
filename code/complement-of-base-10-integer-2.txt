

int bitwiseComplement(int n){
    int copy=n;
    int count = 0;
    int mask = 1;
    if(n==0) return 1;
    for(;copy!=1;)
    {
        copy = copy >> 1;
        mask = (mask<<1) | 1;
        if(copy==1)
            break;
    }
    return (n^mask);
}