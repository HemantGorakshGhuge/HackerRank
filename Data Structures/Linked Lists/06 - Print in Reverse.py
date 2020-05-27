

# Complete the reversePrint function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#

def reversePrint(head):
    reverseList = []
    if head:
        current_node = head
        while(current_node):
            reverseList.append(current_node.data)
            current_node = current_node.next
        while(reverseList):
            element = reverseList.pop()
            print(element)
    else:
        print(None)

