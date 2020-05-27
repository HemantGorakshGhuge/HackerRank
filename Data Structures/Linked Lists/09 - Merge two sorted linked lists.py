

# Complete the mergeLists function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def mergeLists(head1, head2):
    dummy = SinglyLinkedListNode(2)
    result = dummy
    current_node1, current_node2 = head1, head2
    flag = True
    if current_node1 == None:
        return current_node2
    elif current_node2 == None:
        return current_node1
    while (current_node1 != None and current_node2 != None):
        if current_node1.data < current_node2.data:
            temp = current_node1
            current_node1 = current_node1.next
        elif current_node1.data > current_node2.data:
            temp = current_node2
            current_node2 = current_node2.next
        else:
            if flag == True: 
                temp = current_node1
                current_node1 = current_node1.next
                flag = False
            else:
                temp = current_node2
                current_node2 = current_node2.next
                flag = True

        result.next = temp
        result = result.next
    result.next = current_node1 or current_node2
    return dummy.next

