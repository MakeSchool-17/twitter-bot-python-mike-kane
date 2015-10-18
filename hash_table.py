from linked_list import LinkedList


class HashTable():
    def __init__(self, table_size=10):
        self.table = []
        self.table_size = table_size
        self.item_count = 0
        # [brian] This is a nitpick, but python programmers would call this
        # variable `_`, to make it clear they're not using it.
        for bucket in range(table_size):
            self.table.append(LinkedList())

    def load_factor(self):
        load = self.item_count / self.table_size
        return load

    def get_bucket(self, key):
        bucket_id = hash(key) % self.table_size
        correct_bucket = self.table[bucket_id]
        return correct_bucket

    def set(self, key, value):
        correct_bucket = self.get_bucket(key)
        correct_bucket.insert_at_head((key, value))
        self.item_count += 1

    def get(self, key):
        correct_bucket = self.get_bucket(key)
        current_node = correct_bucket.head
        while current_node.data is not None:
            if key in current_node.data:
                return current_node.data
            else:
                current_node = current_node.next_node
        return KeyError("This key is not in this list!")
        # [brian] If a user were to wrap a call to this method in a try-catch
        # block the catch would never be triggered. Instead you should:
        raise KeyError("This key is not in this list!")


    def update(self, key, new_value):
        correct_bucket = self.get_bucket(key)
        current_node = correct_bucket.head
        found = False
        while not found and current_node.data is not None:
            if key in current_node.data:
                found = True
                current_node.data = (key, new_value)
                return '{} updated to {}'.format(key, new_value)
            else:
                current_node = current_node.next_node
        return KeyError('Cannot update: key not in list!')


ht = HashTable()
ht.set('a', 1)
ht.set('b', 2)
print(ht.get('a'))  # => 1
print(ht.get('b'))  # => 2
ht.update('a', 5)
ht.update('b', 1)
print(ht.get('a'))  # => 5
print(ht.get('b'))  # => 1   Phew--it finally works!
