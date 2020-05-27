# Complete the sortedInsert function below.

#
# For your reference:
#
# DoublyLinkedListNode:
#     int data
#     DoublyLinkedListNode next
#     DoublyLinkedListNode prev
#
#
def sortedInsert(head, data):
    current_node = head

    insertion_node = DoublyLinkedListNode(data)
    
    while(current_node and current_node.data < data):
        tail = current_node
        current_node = current_node.next
    
    if not(current_node):
        print(tail.data, data)
        print("add node at last place")
        tail.next = insertion_node
        insertion_node.prev = tail
        

    elif current_node == head:
        print(head.data, data)
        print("add node at first place")
        head.prev = insertion_node
        insertion_node.next = head
        head = insertion_node

    else:    
        print(current_node.data, data)
        print("Normal Case insert node between two node")
        right_node = current_node
        left_node = current_node.prev
        insertion_node.prev = left_node
        insertion_node.next = right_node
        left_node.next = insertion_node
        right_node.prev = insertion_node    


    return head

