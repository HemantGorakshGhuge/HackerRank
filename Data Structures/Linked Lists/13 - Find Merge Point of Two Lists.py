# Complete the findMergeNode function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#


def findMergeNode(head1, head2):
    current_node1 = head1
    current_node2 = head2
    length1 = 0
    length2 = 0

    # finding the total length of each linked list
    while(current_node1 != None or current_node2 != None):
        if current_node1:
            print(current_node1.data)
            current_node1 = current_node1.next
            length1 += 1
        if current_node2:
            print(current_node2.data)
            current_node2 = current_node2.next
            length2 += 1

    print(length1, length2)
    # Finding a common starting point
    checkpoint = min(length1, length2)
    print(checkpoint)

    start_position1 = length1 - checkpoint
    start_position2 = length2 - checkpoint

    current_position1 = 0
    current_position2 = 0
    print(start_position1, start_position2)
    current_node1 = head1
    current_node2 = head2

    # Iterating till start point with respect to both the linked list
    while (current_position1 < start_position1 or current_position2 < start_position2):
        if current_position1 < start_position1:
            current_node1 = current_node1.next
            current_position1 += 1
        if current_position2 < start_position2:
            current_node2 = current_node2.next
            current_position2 += 1
    print(current_position1, current_position2)

    if current_position1 == 0 and current_position2 == 0:
        current_node1 = current_node1.next
        current_node2 = current_node2.next   

    while(current_node1 and current_node2):
        print("value 1 =", current_node1.data)
        print("value 2 =", current_node2.data)
        if current_node1 == current_node2:
            return current_node1.data
        current_node1 = current_node1.next
        current_node2 = current_node2.next

