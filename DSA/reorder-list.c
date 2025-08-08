// Aim: Reorder a singly linked list in-place such that nodes are arranged as
// first node, last node, second node, second last node, and so on.

void reorderList(struct ListNode* head) {
    if (!head || !head->next || !head->next->next) return;

    struct ListNode *slow = head, *fast = head;
    while (fast->next && fast->next->next) {
        slow = slow->next;
        fast = fast->next->next;
    }

    struct ListNode *prev = NULL, *curr = slow->next, *next;
    while (curr) {
        next = curr->next;
        curr->next = prev;
        prev = curr;
        curr = next;
    }
    slow->next = NULL;

    struct ListNode *first = head, *second = prev;
    struct ListNode *tmp1, *tmp2;
    while (second) {
        tmp1 = first->next;
        tmp2 = second->next;

        first->next = second;
        second->next = tmp1;

        first = tmp1;
        second = tmp2;
    }
}
