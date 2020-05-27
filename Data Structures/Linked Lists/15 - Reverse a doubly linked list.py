# Complete the reverse function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def reverse(head):
    current_node = head
    while(current_node):
        last_node = current_node
        current_node = current_node.next
    print(last_node.data)
    new_head = last_node
    current_node = new_head
    while(current_node):
        current_node.prev, current_node.next = current_node.next, current_node.prev
        current_node = current_node.next
    return new_head

