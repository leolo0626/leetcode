/**
 * Definition for singly-linked list.
 struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
     ~LinkedList() {
        while (head != nullptr) {
            ListNode* toDelete = head;
            head = head->next;
            delete toDelete;
        }
    }
 * };
 */

 struct ListNode {
      int val;
      ListNode *next;
      ListNode() : val(0), next(nullptr) {}
      ListNode(int x) : val(x), next(nullptr) {}
      ListNode(int x, ListNode *next) : val(x), next(next) {}
 };


class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* result = new ListNode();
        ListNode* temp = result;
        int next = 0;
        while(l1 != nullptr || l2 != nullptr || next) {
            int l1_v, l2_v ;
            if (l1 == nullptr) {
                l1_v = 0;
            } else {
                l1_v = l1->val;
                l1 = l1->next;
            }

            if (l2 == nullptr) {
                l2_v = 0;
            } else {
                l2_v = l2->val;
                l2 = l2->next;
            }
            
            ListNode* newNode = new ListNode((l1_v + l2_v + next) % 10);
            next = (l1_v + l2_v + next) / 10;
            
            temp->next = newNode;
            temp = temp->next;
        }

        temp = result;
        result = result->next;
        delete temp;
        return result;
    }
};