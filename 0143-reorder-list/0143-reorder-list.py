class Solution:
    def reorderList(self, head):
        if not head or not head.next:
            return
        
       
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        
        
        second = slow.next
        slow.next = None
        
        prev = None
        while second:
            temp = second.next
            second.next = prev
            prev = second
            second = temp
        
        
        first, second = head, prev
        while second:
            temp1 = first.next
            temp2 = second.next
            
            first.next = second
            second.next = temp1
            
            first = temp1
            second = temp2