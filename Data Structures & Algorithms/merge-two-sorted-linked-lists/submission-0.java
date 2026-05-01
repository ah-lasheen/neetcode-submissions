/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */

class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode front = new ListNode();
        ListNode tail = front;

        // both lists have items in them
        while (list1 != null && list2 != null) {
            // if lower list val is less or equal, put that pointer to the start of other list
            if (list1.val <= list2.val) {
                tail.next = list1;
                list1 = list1.next;
            }
            else {
                tail.next = list2;
                list2 = list2.next;
            }
            tail = tail.next;
        }

        // if list1 has no items but list2 still does
        if (list1 == null && list2 != null) {
            // tail.next would go to list2
            tail.next = list2;
        } else if (list2 == null && list1 != null){
            tail.next = list1;
        }

        return front.next;
    }
}