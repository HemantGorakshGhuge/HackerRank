

# Complete the deleteNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

def deleteNode(head, position):
    current_position = 0
    current = head
    if position == 0:
        head = current.next
    else:
        while(current and current_position < position):
            if current_position == position-1:
                current.next = current.next.next
            current = current.next
            current_position += 1
    return head

