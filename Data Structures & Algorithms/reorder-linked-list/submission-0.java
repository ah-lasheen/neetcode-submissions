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
    public void reorderList(ListNode head) {
        // n <= 2 (doesnt need ordering so return)
        if (head == null || head.next == null) return;

        // 1st. get midpoint with slow fast pointers
        ListNode slow = head, fast = head;
        
        // Sample input: [2, 4, 6, 8]
        // Expected: (Only one iteration fast.next.next -> 6)
        //           
        //               [2, 4, 6, 8] : slow.next -> 6
        //
        // Using slow.next we can point to the list to reverse
        while (fast.next != null && fast.next.next != null) { 
            fast = fast.next.next;
            slow = slow.next;
        }

        // 2nd. reverse second list
        ListNode prev = null;
        ListNode curr = slow.next;

        // severing tie between two lists
        slow.next = null;

        ListNode next = null;

        while (curr != null) {
            next = curr.next;
            curr.next = prev;
            prev = curr;
            curr = next;
        }

        // 3rd. merge first and second list in alternating order
        ListNode first = head;  // first string
        ListNode second = prev; // second string (reversed) 

        while (second != null) {
            ListNode next1 = first.next;
            ListNode next2 = second.next;

            first.next = second;
            second.next = next1;

            first = next1;
            second = next2;
        }
    }
}
