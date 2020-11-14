import math
from collections import deque
from typing import List
import collections
from ListNode import ListNode


# URL:
# https://leetcode.com/problems/palindrome-linked-list/

# Question:
# Given a singly linked list, determine if it is a palindrome.

# Definition for singly-linked list.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    @classmethod
    def list2linkedlist(cls, int_list: List[int]):
        head = ListNode(int_list[0])
        current = head
        for num in int_list[1:]:
            temp = ListNode(num)
            current.next = temp
            current = current.next
        return head


# Runtime: 160 ms
# Memory: 24.1 MB
class PalindromeLinkedList:
    @classmethod
    def my_solution(cls, head: ListNode) -> bool:
        temp_list = []
        temp = head

        while temp != None:
            temp_list.append(temp.val)
            temp = temp.next

        while len(temp_list) > 1:
            if temp_list.pop(0) != temp_list.pop(-1):
                return False

        return True

    # Runtime: 72 ms
    # Memorey: 24.1 MB
    @classmethod
    def deque(cls, head: ListNode) -> bool:
        dq: Deque = collections.deque()
        temp = head
        while temp != None:
            dq.append(temp.val)
            temp = temp.next
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True

    @classmethod
    def tortoise_hare(cls, head: ListNode) -> bool:
        tortoise = hare = head
        counter = None

        while hare and hare.next:
            hare = hare.next.next
            counter, counter.next, tortoise = tortoise, counter, tortoise.next

        if hare:
            tortoise = tortoise.next
            while counter and counter.val == tortoise.val:
                tortoise = tortoise.next
                counter = counter.next
        return not counter


def main():
    head = ListNode.list2linkedlist([1, 2, 3, 4, 5, 4, 3, 2, 1])
    # print(PalindromeLinkedList.my_solution(head))
    print(PalindromeLinkedList.tortoise_hare(head))


if __name__ == "__main__":
    main()