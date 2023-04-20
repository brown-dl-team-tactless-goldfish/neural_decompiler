struct am{int number, val;};

int cmp(const void *x, const void *y){
    return ((struct am*)x)->val - ((struct am*)y)->val;
}

int getKth(int lo, int hi, int k){
    struct am *result = (struct am*)malloc(sizeof(struct am)*((hi-lo)+1));
    int count = 0;
    for(int i = lo;i<=hi;i++){
        int value = i;
        int power = 0;
        while(value!=1){
            value = value%2==0 ? value/2 : value*3+1;
            power++;
        }
        result[count].val = power;
        result[count].number = i;
        count++;
    }
    qsort(result, count, sizeof(const struct am), cmp);
    return result[k-1].number;
}






// int cmpfunc (const void * a, const void * b) {
//    return ( *(int*)a - *(int*)b );
// }

// int getKth(int lo, int hi, int k){
// int count=0,j=0;
//     int *ans=(int*)malloc(sizeof(int)*(hi+1-lo));
//     for(int num=lo;num<=hi;num++)
//     {
//         while(num!=1)
//         {
//             if(num%2==0)
//             {
//                 num=num/2;
//                 count++;
//             }
//             else
//             {
//                 num=num*3+1;
//                 count++;
//             }
//         }
//         ans[j]=count;
//         j++;
//     }
//     qsort(ans, hi+1-lo, sizeof(int), cmpfunc);
//     return ans[k-1];
// }