class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


def make_list(elements):
    head = Node(elements[0])
    for element in elements[1:]:
        ptr = head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(element)
    return head


class Solution(object):
    def isPalindrome(self, head):
        fast, slow = head, head
        rev = None
        flag = 1
        if not head:
            return True
        while fast and fast.next:
            if not fast.next.next:
                flag = 0
                break
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = rev
            rev = temp
        fast = slow.next
        slow.next = rev
        if flag:
            slow = slow.next
        while fast and slow:
            if fast.data != slow.data:
                return False
            fast = fast.next
            slow = slow.next
        return True


txt = input("Enter TestCase:")
lst = list(txt)
head = make_list(lst)
obs = Solution()
if obs.isPalindrome(head):
    print("Palindrome")
else:
    print("Not A Palindrome")
