"""
 Address: https://leetcode-cn.com/problems/add-two-numbers/
 Thinking: 1.链表形式表达没想明白。 猜测本题的关键点可能在满10进1上。涉及到链表的操作(访问和修改)
           remark.看完题目解析，明白ListNode即是结点，通过next 访问下一结点。重要的是，我们一开始并不需要知道所有元素，只要头结点就可以代表整条链表，同时双链表相加要考虑链表长度问题。
           想到递归生成，有两种方式，一种是已经想到的，ListNode(,ListNode) 构造结构时候，这个用while，同时要反序输出，借助cur。 另一种是 addTowNumbers 递归
 Test:
 Review:
    链表:
        单链表，双链表，循环链表，指针，头结点 ，头插，尾插
"""

# Definition for singly-linked list.
import math


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        cur = ListNode()
        head = cur
        while l1 or l2 or carry:
            n1, n2 = 0, 0
            if l1:
                n1 = l1.val
                l1 = l1.next
            if l2:
                n2 = l2.val
                l2 = l2.next
            cur.next = ListNode((n1 + n2 + carry) % 10)
            cur = cur.next
            carry = math.floor((n1 + n2 + carry) / 10)
            print(n1 + n2 + carry)
        return head.next


class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None
        if l1 is None:
            l1 = ListNode(0, None)
        if l2 is None:
            l2 = ListNode(0, None)
        if l1.val + l2.val > 9:
            node = l1.next if l1.next else l2.next
            if node:
                node.val = node.val + 1
            else:
                l1.next = ListNode(1, None)
        return ListNode((l1.val + l2.val) % 10, self.addTwoNumbers(l1.next, l2.next))


s = Solution()
nums = [3, 3]
target = 6
# print(s.addTwoNumbers(nums, target))
