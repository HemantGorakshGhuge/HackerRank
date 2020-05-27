# Complete the has_cycle function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def has_cycle(head):
    current_node = head
    values = []
    nexts = []
    if current_node:
        while(current_node):
            print(current_node.data)
            if current_node.data in values and current_node.next in nexts:
                return True
            values.append(current_node.data)
            nexts.append(current_node.next)
            current_node = current_node.next
        return False
    else:
        return None

