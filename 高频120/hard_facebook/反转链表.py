# 详细版
def reverse01(head):
    if head is None:
        return None
    # 分别用p,q两个指针指定先后两个节点
    p = head
    q = head.next

    # 将p节点反转，head节点只能指向None
    p.next = None

    # 当存在多个后续节点时，循环执行
    while q:
        r = q.next  # 用r表示后面未反转节点
        q.next = p  # q节点反转指向p
        p = q
        q = r  # p,q节点后移一位，循环执行后面的操作
    return p


# 精简版
def reverse02(head):
    if not head:
        return None
    p, q, p.next = head, head.next, None
    while q:
        q.next, p, q = p, q, q.next
        return p
