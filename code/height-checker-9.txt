int cmpfunc (const void * a, const void * b) {
   return ( *(int*)a - *(int*)b );
}

int heightChecker(int* heights, int heightsSize){
int count=0;
    int *ans=(int *)malloc(sizeof(int)*heightsSize);
    for(int i=0;i<heightsSize;i++)
    {
        ans[i]=heights[i];
    }
    qsort(heights, heightsSize, sizeof(int), cmpfunc);
    for(int j=0;j<heightsSize;j++)
    {
        if(heights[j]!=ans[j])
        {
            count++;
        }
    }
    return count;
}