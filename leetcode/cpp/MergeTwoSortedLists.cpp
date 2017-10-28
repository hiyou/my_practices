//
// Created by zz on 2017/10/27.
// Time:  O(n)
// Space: O(1)


struct ListNode {
    int val;
    ListNode *next;

    ListNode(int x) : val(x), next(nullptr) {}
};

class Solution {
public:
        ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) {
            ListNode dummy{0};
            ListNode *curr = &dummy;

            while (l1 && l2) {

                if (l1->val < l2->val) {
                    curr->next = l1;
                    l1 = l1->next;
                } else {
                    curr->next = l2;
                    l2 = l2->next;
                }

                curr = curr->next;

            }

            curr->next = l1 ? l1 : l2;
            return dummy.next;
        }
    };

