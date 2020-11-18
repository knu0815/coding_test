import math
from collections import deque
from typing import List
import collections
from ListNode import ListNode

# URL:
# https://leetcode.com/problems/odd-even-linked-list/

# Question:
# Given a singly linked list,
# group all odd nodes together followed by the even nodes.
# Please note here we are talking about the node number and not the value in the nodes.

# You should try to do it in place.
# The program should run in O(1) space complexity and O(nodes) time complexity.
class OddEvenLinkedList:

    # Runtime: 44 ms
    # Memory: 15.7 MB
    @classmethod
    def my_solution(cls, head: ListNode) -> ListNode:
        if head is None:
            return None

        odd = head
        even = head.next
        even_head = head.next

        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next

        odd.next = even_head
        return head


def main():
    list2 = ListNode.list2linkedlist([1, 2, 3, 4])
    answer = ListNode.list2linkedlist([2, 3, 2, 4])
    res = OddEvenLinkedList.my_solution(list2)
    print(ListNode.linkedlist2list(res))


if __name__ == "__main__":
    main()
