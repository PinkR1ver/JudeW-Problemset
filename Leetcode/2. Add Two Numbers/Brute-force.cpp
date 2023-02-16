#include <iostream>

using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
};

class Solution
{
public:
    ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
    {
        ListNode *ptr1 = l1;
        ListNode *ptr2 = l2;
        int bit_val = (ptr1->val + ptr2->val) % 10;
        int carry_next = (ptr1->val + ptr2->val) / 10;
        ListNode* res = new ListNode(bit_val);
        ListNode* position = res;
        int val1, val2;
        for (; ptr1->next != NULL || ptr2->next != NULL || carry_next != 0;) {
            if(ptr1->next != NULL) {
                ptr1 = ptr1->next;
                val1 = ptr1->val;
            }
            else val1 = 0;
            if(ptr2->next != NULL) {
                ptr2 = ptr2->next;
                val2 = ptr2->val;
            }
            else val2 = 0;
            bit_val = (val1 + val2 + carry_next) % 10;
            carry_next = (val1 + val2 + carry_next) / 10;
            ListNode* node = new ListNode(bit_val);
            position->next = node;
            position = position->next;
        }
        return res;
    }
};

int main()
{
    return 0;
}