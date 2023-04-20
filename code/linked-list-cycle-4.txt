bool hasCycle(struct ListNode *head) {
    // pointer used to traverse one node
    struct ListNode* slow = head, *fast = head;
    
    // Traverse to find the loopNode
    while (fast && fast->next)     {
        slow = slow->next;
        fast = fast->next->next;
        if(slow == fast)
            return true;
    }
    return false;
}