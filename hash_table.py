from linked_list_class import Linked_List


class Hash_Table():
    def __init__(self, table_size=10):
        self.table = []
        self.table_size = table_size
        self.item_count = 0
        for bucket in range(table_size):
            self.table.append(Linked_List())

    def load_factor(self):
        load = self.item_count / self.table_size
        return load

    def get_bucket(self, key):
        bucket_id = hash(key) % self.table_size
        correct_bucket = self.table[bucket_id]
        return correct_bucket

    def set(self, key, value):
        correct_bucket = self.get_bucket(key)
        correct_bucket.insert((key, value))

    def get(self, key):
        correct_bucket = self.get_bucket(key)
        return correct_bucket.search(key)

    def update(self, key, value):
        correct_bucket = self.get_bucket(key)
        data = correct_bucket.search(key)
        data = (key, value)
        return "{}'s value updated to {}".format(data[0], data[1])

    def keys(self):
        keys = []
        for bucket in self.table:
            for data in bucket:
                keys.append(data[0])
        return keys

    def values(self):
        list_of_keys = self.keys()
        values_to_return = []
        for key in list_of_keys:
            values_to_return.append(self.get(key))
        return values_to_return
