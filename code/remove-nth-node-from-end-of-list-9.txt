struct ListNode* removeNthFromEnd(struct ListNode* head, int n){
    struct ListNode *p=head, *q=head;
	// delay by n nodes.
    for(int i=0; i<n; i++) {
        p = p->next;
    }
    if(!p) {
        //remove head
        return head->next;
    }
	// pass through
    while(p->next) {
        p = p->next;
        q = q->next;
    }
    q->next = q->next->next;
    return head;
}