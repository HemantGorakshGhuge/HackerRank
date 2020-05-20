

# Complete the reverse function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#

# 1>2>3>4>None
def reverse(head):
    if head:
        current_node = head #1 = head
        next_node = current_node.next   #next_node = 2 = 1.next   
        current_node.next = None    #1.next = None
        while(next_node):   #next_node = 2
            temp = next_node.next   #temp = 2.next = 3
            next_node.next = current_node   #2.next = 1, 2>1
            head = current_node = next_node #head = current_node = 2
            next_node = temp    #next_node = 3

    return head
