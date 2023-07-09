#include "add_two_numbers.cpp"
#include <iostream>
// g++ -std=c++11 -o add_two_numbers main.cpp

int main() {
    ListNode* l1 = new ListNode(2, new ListNode(4, new ListNode(3)));
    ListNode* l2 = new ListNode(5, new ListNode(6, new ListNode(4)));

    Solution solution;
    ListNode* result = solution.addTwoNumbers(l1, l2);
    while (result != nullptr) {
        std::cout << result->val <<std::endl;
        result = result->next;
    }

    // Delete all ListNode objects in l1
    ListNode* current = l1;
    while (current != nullptr) {
        ListNode* toDelete = current;
        std::cout << "To Delete: " << toDelete << " : " << current -> val << std::endl;
        current = current->next;
        delete toDelete;
    }

    // Delete all ListNode objects in l2
    current = l2;
    while (current != nullptr) {
        ListNode* toDelete = current;
        current = current->next;
        delete toDelete;
    }

    // Delete all ListNode objects returned by addTwoNumbers
    current = result;
    while (current != nullptr) {
        ListNode* toDelete = current;
        current = current->next;
        delete toDelete;
    }

}