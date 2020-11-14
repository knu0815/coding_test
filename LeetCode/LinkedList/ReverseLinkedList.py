from typing import List
import collections
from ListNode import ListNode


# URL:
# https://leetcode.com/problems/reverse-linked-list/

# Question:
# Reverse a singly linked list.

# Runtime: 32 ms
# Memorey: 15.6 MB
class ReverseLinkedList:
    @classmethod
    def my_solution(cls, head: ListNode) -> ListNode:
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev


def main():
    h1 = ListNode.list2linkedlist([1, 2, 3, 4, 5])
    answer = ReverseLinkedList.my_solution(h1)
    print(ListNode.linkedlist2list(answer))


if __name__ == "__main__":
    main()