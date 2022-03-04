# Time O(n) | Space O(1)
# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def shiftLinkedList(head, k):
    if not head or not head.next:
        return head

    dummy = LinkedList(-1)
    prev = dummy
    prev.next = head

    length = 0
    while prev.next:
        prev = prev.next
        length += 1
    tail = prev

    if k % length == 0:
        return head
    if k < 0:
        steps = abs(k) % length
    if k > 0:
        steps = length - (k % length)

    p1 = dummy
    p1.next = head
    for _ in range(steps):
        p1 = p1.next

    new_head = p1.next
    p1.next = None

    tail.next = dummy.next
    return new_head




