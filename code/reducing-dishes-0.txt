int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int maxSatisfaction(int* satisfaction, int satisfactionSize){
qsort(satisfaction, satisfactionSize, sizeof(int), cmpfunc);
    int max=0;
    for(int i=0;i<satisfactionSize;i++)
    {
        int k=1;
        int sum=0;
        for(int j=i;j<satisfactionSize;j++)
        {
            sum+=satisfaction[j]*k;
            k++;
        }
        if(sum>max)
        {
            max=sum;
        }
    }
    return max;
}