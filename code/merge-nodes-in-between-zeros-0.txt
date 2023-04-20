struct ListNode* mergeNodes(struct ListNode* head) {

	head = head->next;
	struct ListNode* traverse = head;

	while (traverse != NULL)
	{
		if (traverse->next != NULL && traverse->next->val != 0)
		{
			traverse->val = traverse->val + traverse->next->val;
			traverse->next = traverse->next->next;
		}
		else 
		{
			traverse->next = traverse->next->next;
			traverse = traverse->next;
		}
	}
	return head;
}
