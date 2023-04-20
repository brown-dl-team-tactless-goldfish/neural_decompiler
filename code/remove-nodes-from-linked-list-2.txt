/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */

struct ListNode* removeNodes(struct ListNode* head){
    int length=0;
    struct ListNode *temp=head;
    while(temp!=NULL){
        length++;
        temp=temp->next;
    }
    printf("length : %d\n",length);
    struct ListNode* stack[length];
    int top=-1;
    while(head!=NULL){
        while(top!=-1 && head->val > stack[top]->val){
            top--;
        }
        stack[++top]=head;
        head=head->next;
    }

    temp=stack[0];
    head=temp;
    for(int i=1;i<top;i++){
        temp->next=stack[i];
        temp=temp->next;
    }
    temp->next=stack[top];
    temp->next->next=NULL;
    return head;
}