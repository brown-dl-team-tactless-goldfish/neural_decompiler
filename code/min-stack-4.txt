typedef struct {
    int top;
    int *val;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack* q=(MinStack*)malloc(sizeof(MinStack));
    q->val=(int*)malloc(sizeof(int)*maxSize);
    q->top=0;
    return q;
}

void minStackPush(MinStack* obj, int x) {
    obj->val[obj->top++]=x;
    
}

void minStackPop(MinStack* obj) {
    obj->top--;
}

int minStackTop(MinStack* obj) {
    return obj->val[obj->top-1];
}

int minStackGetMin(MinStack* obj) {
    int min=INT_MAX;
    for(int i=0;i<obj->top;i++){
        if(min>obj->val[i]){
            min=obj->val[i];
        }
    }
    return min;
}

void minStackFree(MinStack* obj) {
    free(obj->val);
    free(obj);
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */