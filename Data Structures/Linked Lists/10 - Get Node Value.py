

# Complete the getNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def getNode(head, positionFromTail):
    current_node = head
    length = 0
    while(current_node):
        current_node = current_node.next
        length += 1
    print(length)
    position = length - positionFromTail - 1
    print(position)
    current_position = 0
    current_node = head
    while(current_node):
        print("hihi")
        if position == current_position:
            return current_node.data
        elif position != current_node:
            current_position += 1
            current_node = current_node.next

