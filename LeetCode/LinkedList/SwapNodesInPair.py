import math
from collections import deque
from typing import List
import collections
from ListNode import ListNode

# URL:
# https://leetcode.com/problems/swap-nodes-in-pairs/

# Question:
# Given a linked list, swap every two adjacent nodes and return its head.
# You may not modify the values in the list's nodes. Only nodes itself may be changed.


class SwapNodesInPair:
    # Runtime: 24 ms
    # Memory: 14.1 MB
    @classmethod
    def my_solution(cls, head: ListNode) -> ListNode:
        if head and head.next:
            temp = head.next
            head.next = cls.my_solution(temp.next)
            temp.next = head
            return temp
        return head

    # Runtime: 24 ms
    # Memory: 14.1 MB
    @classmethod
    def my_solution2(cls, head: ListNode) -> ListNode:
        root = prev = ListNode(None)
        prev.next = head
        while head and head.next:
            temp = head.next
            head.next = temp.next
            temp.next = head

            prev.next = temp
            head = head.next
            prev = prev.next.next
        return root.next


def main():
    list2 = ListNode.list2linkedlist([1, 2, 3, 4])
    answer = ListNode.list2linkedlist([2, 1, 4, 3])
    res = SwapNodesInPair.my_solution2(list2)
    print(ListNode.linkedlist2list(res))


if __name__ == "__main__":
    main()