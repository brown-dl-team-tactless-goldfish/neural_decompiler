/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */


struct ListNode* oddEvenList(struct ListNode* head)
{
    if(head == NULL)            //No Node
        return head;
    
    if(head->next == NULL)      //One Node
        return head;
    
    if(head->next->next == NULL) //Two Node
        return head;
    
    struct ListNode * prev_ptr = head;
    struct ListNode * current_ptr = head->next;
    struct ListNode * next_ptr = head->next->next;
    
    struct ListNode * stored_ptr = current_ptr;
    
    while((current_ptr != NULL) && (current_ptr->next != NULL))
    {
        prev_ptr->next = next_ptr;
        
        if(next_ptr!=NULL)
            current_ptr->next = next_ptr->next;
        
        prev_ptr = next_ptr;
        
        if(next_ptr!=NULL)
            current_ptr = next_ptr->next;
        
        if(next_ptr->next != NULL)
            next_ptr = next_ptr->next->next;  
        else
            next_ptr = NULL;
    }
    
    if((current_ptr == NULL) && (next_ptr == NULL)) //Odd number of elements
    {
        prev_ptr->next = stored_ptr;

    }
    
    else if((current_ptr->next == NULL) && (next_ptr == NULL))  //Even number of elements
    {
        prev_ptr->next = stored_ptr;
    }
    return head;
    
}