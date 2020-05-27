# Complete the removeDuplicates function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def removeDuplicates(head):
    current_node = head
    if current_node:
        while(current_node and current_node.next):
            if current_node.data == current_node.next.data:
                current_node.next = current_node.next.next
            else:
                current_node = current_node.next
    else:
        return None
    return head
