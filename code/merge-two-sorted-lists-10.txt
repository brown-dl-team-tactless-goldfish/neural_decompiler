struct ListNode* mergeTwoLists(struct ListNode* a, struct ListNode* b) {
    if (!a || b && a->val > b->val) a += b - (b = a);
    if (a) a->next = mergeTwoLists(a->next, b);
    return a;
}