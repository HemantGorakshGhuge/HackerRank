# Complete the insertNodeAtPosition function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next

def insertNodeAtPosition(head, data, position):
    current_position = 0
    current = head
    node = SinglyLinkedListNode(data)
    
    while current and current_position <= position:
        if current_position == position - 1:
            node.next = current.next
            current.next = node
        current = current.next
        current_position += 1

    return head
