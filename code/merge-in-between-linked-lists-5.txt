struct ListNode* mergeInBetween(struct ListNode* list1, int a, int b, struct ListNode* list2){
    struct ListNode* p, *q;
    p = list1;
    q = list1;
    while(a > 1){
        a--;
        p = p->next;
    }
    
    while(b){
        b--;
        q = q->next;
    }
    
    p->next = list2;
    struct ListNode* x = list2;
    while(x->next){
        x = x->next;
    }
    x->next = q->next;
    q->next = NULL;
    
    return list1;
}