/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
int depth(struct ListNode* head){
    int d = 0;
    struct ListNode* tmp = head;
    while(tmp){
        d++;
        tmp = tmp->next;
    }
    return d;
}
struct ListNode* removeNodes(struct ListNode* head){
    int n = depth(head);
    struct ListNode** arr = malloc(n * sizeof(struct ListNode*));
    struct ListNode* tmp = head;
    int i = 0;
    while(tmp){
        arr[i] = tmp;
        i++;
        tmp = tmp->next;
    }
    bool* rm = calloc(n, sizeof(bool));
    int max = arr[n-1]->val;
    for(int i = n-2; i >=0; i--){
        if(arr[i]->val < max)
            rm[i] = true;
        else if(arr[i]->val > max)
            max = arr[i]->val;
    }
    struct ListNode* ans ;
    for(int i = 0; i < n; i++){
        if(rm[i] == false){
            ans = arr[i];
            tmp = ans;
            for(int j = i+1; j < n; j++){
                if(rm[j] == false){
                    tmp->next = arr[j];
                    tmp = tmp->next;
                }
            }
            tmp->next = NULL;
            break;
        }
    }
    free(arr);
    return ans;
}