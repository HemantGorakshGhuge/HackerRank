

# Complete the compare_lists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def compare_lists(llist1, llist2):
    current_node1 = llist1
    current_node2 = llist2
    if current_node1 and current_node2:
        while(current_node1 and current_node2):
            if current_node1.data == current_node2.data:
                current_node1 = current_node1.next
                current_node2 = current_node2.next
            else:
                return 0
        if current_node1 == current_node2:
            return 1 
        return 0
    if current_node1.data == current_node2.data:
        return 1



