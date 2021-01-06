"""
 Address: https://leetcode-cn.com/problems/add-two-numbers/
 Thinking: 1.链表形式表达没想明白。 猜测本题的关键点可能在满10进1上。涉及到链表的操作(访问和修改)
           remark.看完题目解析，明白ListNode即是结点，通过next 访问下一结点。重要的是，我们一开始并不需要知道所有元素，只要头结点就可以代表整条链表，同时双链表相加要考虑链表长度问题。
 Test:
 Review:
    链表:
        单链表，双链表，循环链表，指针，头结点 ，头插，尾插
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1:
            l1.val

"""
Reference:
    solution: 由于输入的两个链表都是逆序存储数字的位数的，因此两个链表中同一位置的数字可以直接相加。
              我们同时遍历两个链表，逐位计算它们的和，并与当前位置的进位值相加。
              具体而言，如果当前两个链表处相应位置的数字为 n1,n2，进位值为 carry，则它们的和为 n1+n2+carry；
              其中，答案链表处相应位置的数字为(n1+n2+carry)%10，而新的进位值为⌊(n1+n2+carry)/10⌋,
              如果两个链表的长度不同，则可以认为长度短的链表的后面有若干个 0。
              此外，如果链表遍历结束后，有 carry>0，还需要在答案链表的后面附加一个节点，节点的值为 carry。
"""





s = Solution()
nums = [3, 3]
target = 6
# print(s.addTwoNumbers(nums, target))
