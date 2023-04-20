int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int maxCoins(int* piles, int pilesSize){
qsort(piles, pilesSize, sizeof(int), cmpfunc);
    int mymax = 0;
    for (int i = pilesSize / 3; i < pilesSize; i += 2)
    {
        mymax += piles[i];
    }
    return mymax;
}