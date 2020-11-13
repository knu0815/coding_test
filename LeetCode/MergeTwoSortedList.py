from typing import List
import collections

# URL:
# https://leetcode.com/problems/merge-two-sorted-lists/

# Question:
# Merge two sorted linked lists and return it as a new sorted list.
# The new list should be made by splicing together the nodes of the first two lists.


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


class MergeTwoSortedList:
    @classmethod
    def my_solution(cls, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1

        if l1:
            l1.next = cls.my_solution(l1.next, l2)

        return l1


def main():
    h1 = ListNode.list2linkedlist([1, 2, 3, 2, 1])
    h2 = ListNode.list2linkedlist([1, 2, 4, 5, 1])
    # print(PalindromeLinkedList.my_solution(head))
    print(MergeTwoSortedList.my_solution(h1, h2))


if __name__ == "__main__":
    main()