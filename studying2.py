"""
Second warm up exercise - implement a LinkedList class and execute. This includes implementation of:
    
    The Node Class
        __init__
        get_data
        get_next
        set_next

    The LinkedList Class which refers to the Node class
        __init__
        insert
        size
        search
        delete
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node
    def get_data(self)
        return self.data
    def get_next(self)
        return self.next_node
    def set_next(self, new_next)
        self.next_node = new_next

class LinkedList(object)
    def __init__(self, head=None)
        self.head = head
    def insert(self, data)
        new_node = Node(data)
        new_node.set_next(self.head)
        self.head = new_node
    
