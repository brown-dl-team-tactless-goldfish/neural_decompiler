/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* addTwoNumbers(struct ListNode* l1, struct ListNode* l2){
    struct ListNode* ret = (struct ListNode*)malloc(sizeof(struct ListNode));
    ret->val = (l1->val + l2->val) % 10;
    ret->next = NULL;   //remember to add this
    int quo = (l1->val + l2->val) / 10;
    struct ListNode* tmp = (struct ListNode*)malloc(sizeof(struct ListNode));
    tmp = ret;
    int c;
    
    while(l1->next != NULL && l2->next != NULL){
        c = l1->next->val + l2->next->val + quo;
        tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next->val = c % 10;
        tmp->next->next = NULL;
        quo = c / 10;
        l1 = l1->next;
        l2 = l2->next;
        tmp = tmp->next;
    }
    
    while(l1->next != NULL){
        c = l1->next->val + quo;
        tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next->val = c % 10;
        tmp->next->next = NULL;
        quo = c / 10;
        l1 = l1->next;
        tmp = tmp->next;
    }
    
    while(l2->next != NULL){
        c = l2->next->val + quo;
        tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next->val = c % 10;
        tmp->next->next = NULL;
        quo = c / 10;
        l2 = l2->next;
        tmp = tmp->next;
    }
    
    if(quo != 0){
        tmp->next = (struct ListNode*)malloc(sizeof(struct ListNode));
        tmp->next->val = quo;
        tmp->next->next = NULL;
    }
    
    return ret;

}