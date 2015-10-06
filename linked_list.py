class Node():

    def __init__(self, data=None):
        self.data = data
        self.next_node = None

    def __str__(self):
        has_next = ', has next' if self.next else ''
        return 'Node({}{})'.format(self.data, has_next)
        # appends each node to a string.  If self.next does not exist (== None)
        # appends '' instead.


class LinkedList():

    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __str__(self):
        head_str = 'head: ' + str(self.head) if self.head else ''
        tail_str = 'tail: ' + str(self.tail) if self.tail else ''
        return 'LinkedList({}{})'.format(head_str, tail_str)
        # returns head node and tail node, as long as they dont == None

    def is_empty(self):
        return self.size == 0
        # returns True only if == 0

    def is_valid(self):
        head_valid = self.head is not None
        tail_valid = self.tail is not None
        size_valid = self.size > 0
        # sets above to bools based on value
        if head_valid and tail_valid and size_valid:
            return True
        elif not head_valid and not tail_valid and not size_valid:
            # still True if all are False, bc its an empty node
            return True
        else:
            return False

    def insert_at_head(self, data):
        # create a new node with  data
        new_node = Node(data)
        new_node.next = self.head
        # ^^reassign head reference to previous head
        self.head = new_node
        # ^^reassign head reference to newly created head
        self.size += 1
        # assign tail reference if list is empty
        if self.tail is None:
            self.tail = new_node

    def insert_at_tail(self, data):
        # create a new node with data
        new_node = Node(data)
        if self.is_empty():
            # assign head reference
            self.head = new_node
        else:
            # append new node after tail
            self.tail.next = new_node           #  ?? Why cant I just assign self.tail to new_node immediately?
        # reassign tail reference
        self.tail = new_node
        self.size += 1

    def remove_head(self):
        if self.head is None:
            raise ValueError('List is empty')  # self-explanatory
        self.head = self.head.next  # since original head is no longer linked, does this mean it is removed?  Isn't it still in memory, or is that not important?
        self.size -= 1

    def calculate_size(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            # when current_node == None, we have hit the end of the linked list
            count += 1
            current_node = current_node.next
        return count


def test_node():
    print('===Node class tests====')
    node1 = Node({'Mike': 4})  # why curly braces here? Does this set type as dict?
    print('node1:', node1)
    node2 = Node(['abe', 'ignat'])  # ^^ same question
    print('node2:', node2)
    node1.next = node2
    node2.next = node1
    print('node1:', node1)
    print('node2:', node2)


def test_linked_list():
    def check_linked_list(ll):
        print('ll:', ll)
        print('ll.is_valid:', ll.is_valid())
        print('ll.calculate_size:', ll.calculate_size)
        print('ll.size:', ll.size)

    print('==== Linked List class tests====')
    ll = LinkedList()
    check_linked_list(ll)
                                            #  pretty sure I understand the tests...
    try:
        ll.remove_head()
    except ValueError as error:
        print('Could not remove head, error:', error)
        check_linked_list(ll)

    ll.insert_at_head('hello')
    check_linked_list(ll)

    ll.insert_at_head('goodbye')
    check_linked_list(ll)

    ll.insert_at_tail('the end')
    check_linked_list(ll)

    ll.remove_head()
    check_linked_list(ll)

if __name__ == '__main__':
    test_node()
    test_linked_list()
