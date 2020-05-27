

# Complete the insertNodeAtTail function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def insertNodeAtTail(head, data):
    node = SinglyLinkedListNode(data)
    if not(head):
        head = node
    else:
        current = head
        while current.next:
            current = current.next
        current.next = node
    return head


