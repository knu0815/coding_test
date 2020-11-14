from typing import List


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

    @classmethod
    def linkedlist2list(cls, head):
        return_list = []
        while head != None:
            return_list.append(head.val)
            head = head.next
        return return_list