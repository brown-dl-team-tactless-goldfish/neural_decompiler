bool hasCycle(struct ListNode *head) {
    struct ListNode * slow=head,*fast=NULL;
    
    if(!head || !(head->next))
        return false;
    
    fast=head->next;
    
    while(slow!=fast)
    {
        if(fast==NULL)
        {
            return false;
        }
        slow=slow->next;
        if(fast->next && fast->next->next)
            fast=fast->next->next;
        else
            fast = fast->next;
    }
    return true;
}