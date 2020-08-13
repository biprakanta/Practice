# https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def get_val(self, link):
        if link:
            return link.val
        return 0
    
    def get_next(self, link):
        if link:
            return link.next
        return
        
    def addTwoNumbers(self, l1, l2):
        new_l = ListNode()
        temp = new_l
        h1 = l1
        h2 = l2
        over=0
        while h1 or h2:
            
            sum= self.get_val(h1) + self.get_val(h2) + over
            temp.val = sum%10
            if sum//10:
                over = sum//10
            else:
                over = 0
 
            h1 = self.get_next(h1)
            h2 = self.get_next(h2)
            if h1 or h2:
                temp.next = ListNode()
                temp = temp.next
        if over:
            temp.next = ListNode(over)

        return new_l
