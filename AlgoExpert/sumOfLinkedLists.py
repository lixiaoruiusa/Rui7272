# O(max(N, M)) time and O(max(N, M)) + 1 space
# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def sumOfLinkedLists(linkedListOne, linkedListTwo):
    l1 = linkedListOne
    l2 = linkedListTwo

    dummy = LinkedList(0)
    current = dummy
    carry = 0

    while l1 or l2 or carry:
        l1_value = l1.value if l1 is not None else 0
        l2_value = l2.value if l2 is not None else 0
        node_value = (l1_value + l2_value + carry) % 10
        new_node = LinkedList(node_value)
        current.next = new_node
        current = new_node
        carry = (l1_value + l2_value + carry) // 10
        l1 = l1.next if l1 is not None else None
        l2 = l2.next if l2 is not None else None
    return dummy.next




