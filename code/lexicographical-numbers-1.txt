/**
 * Note: The returned array must be malloced, assume caller calls free().
 */
void dfs(int *res,int *pos,int cur,int n){
    if(cur>n) return;
    else{
        res[(*pos)++]=cur;
        
        for(int j=0;j<10;j++){
            int temp=cur*10+j;
            if(temp > n) return;
            dfs(res,pos,temp,n);
        }
    }
}
int* lexicalOrder(int n, int* returnSize){
    *returnSize=n;
    int *res=(int*)malloc(sizeof(int)*n);
    int pos=0;
    for(int i=1;i<10;i++){
        dfs(res,&pos,i,n);
    }
    return res;
}