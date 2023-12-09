'''给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

你可以假设除了数字 0 之外，这两个数都不会以 0 开头。'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #对于l1和l2有三种情况：一是l1为空直接返回l2，l2为空直接返回l1，l1和l2都为空，直接返回空
        if l1 is None:
            return l2
        if l1 is None:
            return l2
        # 当l1、l2都不为空的时候，可以进行运算，进行运算有三种情况：一是l1长度比l2长，二是l2长度比l1长，三是两者一样长
        sum_2 = ListNode()
        p=sum_2
        carry = 0
        while l1 and l2:
            p.next = ListNode((l1.val+l2.val+carry)%10)
            carry = (l1.val+l2.val+carry)//10
            p=p.next
            l1 = l1.next
            l2 = l2.next
        if l1:
            while l1:
                p.next = ListNode((l1.val+carry)%10)
                carry = (l1.val+carry)//10
                l1=l1.next
                p = p.next
        if l2:
            while l2:
                p.next = ListNode((l2.val+carry)%10)
                carry = (l2.val+carry)//10
                l2=l2.next
                p = p.next
        if carry>0:
            p.next = ListNode(carry)
        return sum_2.next
