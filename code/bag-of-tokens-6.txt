int cmp(void* a, void* b){
    return *(int*)a-*(int*)b;
}
int bagOfTokensScore(int* tokens, int tokensSize, int P) {
    qsort(tokens, tokensSize, sizeof(int), cmp);
    int left=0;
    int right=tokensSize-1;
    int point=0;
    int max=0;
    while(left<=right){
        if(tokens[left]<=P){
            P-=tokens[left];
            point++;
            left++;
        }else if(point>0){
            P+=tokens[right];
            point--;
            right--;
        }else{
            break;
        }
        max=max>point?max:point;
    }
    return max;
}