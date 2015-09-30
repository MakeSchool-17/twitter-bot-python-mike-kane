

class Node():

    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next_node = next

    def get_next(self):
        return self.next_node
