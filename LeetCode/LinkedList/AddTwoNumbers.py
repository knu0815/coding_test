import math
from collections import deque
from typing import List
import collections
from ListNode import ListNode

# URL:
# https://leetcode.com/problems/add-two-numbers/

# Question:
# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.


class AddTwoNumbers:

    # Runtime: 68 ms
    # Memory: 14.1 MB
    @classmethod
    def my_solution(cls, l1: ListNode, l2: ListNode) -> ListNode:
        sum = 0
        head = n = ListNode(0)
        while l1 or l2 or sum:
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next
            sum, val = divmod(sum, 10)
            n.next = ListNode(val)
            n = n.next
        return head.next

    @classmethod
    def 

def main():
    list1 = ListNode.list2linkedlist([9, 9, 9, 9, 9, 9, 9])
    list2 = ListNode.list2linkedlist([9, 9, 9, 9])
    answer = ListNode.list2linkedlist([4, 4, 4])
    res = AddTwoNumbers.my_solution(list1, list2)
    print(ListNode.linkedlist2list(res))


if __name__ == "__main__":
    main()
