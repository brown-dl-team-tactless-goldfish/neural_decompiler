typedef struct Node{
    int val;
    struct Node *next;
}Node,*Linklist;

typedef struct Ret{
    int *s;
    struct Ret *next;
}Ret, *Retlist;

Retlist Create(){
    Retlist head=(Retlist)malloc(sizeof(Ret));
    head->next=NULL;
    return head;
}

Linklist CreateLink(int *s, int n){
    Linklist head,node,end;
    head=(Linklist)malloc(sizeof(Node));
    head->next=NULL;
    head->val=NULL;
    end=head;
    for(int i=0;i<n;i++){
        node=(Linklist)malloc(sizeof(Node));
        node->val=s[i];
        end->next=node;
        end=node;
        end->next=NULL;
    }
    return head;
}
void Do(Linklist list,int n, int nn,int *record, int lier, int *count, Retlist *ret){
    int i,j,k;
    Linklist t=list, pre=t;
    for(i=0;i<n;i++){        
        pre=t;
        t=t->next;
        if(i>0){
            if(t->val==pre->val){
                continue;
            }
        }
        record[lier]=t->val;
        pre->next=t->next;
        if(n==1){            
            Retlist node=Create();
            node->s=(int*)malloc(nn*sizeof(int));
            for(i=0;i<nn;i++){
                node->s[i]=record[i];
            }
            (*ret)->next=node;
            (*ret)=node;
            (*count)++;
        }
        else Do(list,n-1, nn, record, lier+1, count, ret);
        t->next=pre->next;
        pre->next=t;
    }
}
void sort(int* nums, int begin, int end)
{
    int l=begin, r=end;
    int v = nums[(l+r)/2];
    while(l <= r)
    {
        while(nums[l] < v) l++;
        while(nums[r] > v) r--;
        if(l <= r)
        {
            int t = nums[l];
            nums[l] = nums[r];
            nums[r] = t;
            l++; r--;
        }
    }
    if(r > begin)
        sort(nums, begin, r);
    if(l < end)
        sort(nums, l, end);
}

int** permuteUnique(int* nums, int n, int* r, int** c){
    sort(nums, 0, n-1);
    int i,j;
    int *record=(int*)calloc(n,sizeof(int));
    int lier=0, h=0, *count=&h;
    Linklist list=CreateLink(nums,n);
    Retlist Ret=Create(), *ret=&Ret;
    Retlist retHead=Ret;
    Do(list,n, n,record, lier, count, ret);
    *r=*count;
    int **s=(int**)calloc((*r),sizeof(int*));
    (*c)=(int*)calloc((*r),sizeof(int));
    for(i=0;i<(*r);i++){
        retHead=retHead->next;
        s[i]=retHead->s;
        (*c)[i]=n;
    }
    return s;
}