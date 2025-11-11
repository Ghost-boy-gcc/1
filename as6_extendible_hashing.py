#Extendible Hashing Implementation

class Bucket:
    def __init__(self, depth, size):
        self.depth = depth
        self.size = size
        self.items = {}

    def is_full(self):
        return len(self.items) == self.size

    def insert(self, key, value):
        self.items[key] = value

    def delete(self, key):
        del self.items[key]

    def search(self, key):
        return self.items.get(key, None)

class ExtendibleHashTable:
    def __init__(self, bucket_size=2):
        self.global_depth = 1
        self.bucket_size = bucket_size
        self.directory = [Bucket(1, self.bucket_size) for _ in range(2)]

    def hash(self, key):
        return key & ((1 << self.global_depth) - 1)

    def insert(self, key, value):
        index = self.hash(key)
        bucket = self.directory[index]

        if not bucket.is_full():
            bucket.insert(key, value)
            print(f"Inserted ({key}, {value}) into bucket {index}")
            return

        print(f"Bucket {index} is full. Splitting...")
        self.split_bucket(index)
        self.insert(key, value) # Retry insertion

    def split_bucket(self, index):
        old_bucket = self.directory[index]
        local_depth = old_bucket.depth

        if local_depth == self.global_depth:
            self.double_directory()

        new_bucket = Bucket(local_depth + 1, self.bucket_size)
        old_bucket.depth += 1
        
        # Update directory pointers
        for i in range(len(self.directory)):
            if self.directory[i] == old_bucket and (i >> local_depth) & 1:
                self.directory[i] = new_bucket
        
        # Rehash items from old bucket
        old_items = list(old_bucket.items.items())
        old_bucket.items.clear()
        for k, v in old_items:
            self.insert(k, v)
    
    def double_directory(self):
        print("Doubling directory size...")
        self.directory.extend(self.directory)
        self.global_depth += 1
    
    def search(self, key):
        index = self.hash(key)
        value = self.directory[index].search(key)
        if value is not None:
            print(f"Found key {key} with value '{value}' in bucket {index}")
        else:
            print(f"Key {key} not found")
        return value

    def delete(self, key):
        index = self.hash(key)
        bucket = self.directory[index]
        if key in bucket.items:
            bucket.delete(key)
            print(f"Key {key} deleted from bucket {index}")
        else:
            print(f"Key {key} not found for deletion.")

    def display(self):
        print("\nIn Directory:")
        seen = set()
        for i, bucket in enumerate(self.directory):
            if id(bucket) not in seen:
                print(f"Bucket {i} (depth = {bucket.depth}): {list(bucket.items.items())}")
                seen.add(id(bucket))

# Example usage
if __name__ == "__main__":
    ht = ExtendibleHashTable(bucket_size=2)
    ht.insert(1, "One")
    ht.insert(2, "Two")
    ht.insert(3, "Three")
    ht.insert(4, "Four")
    ht.insert(5, "Five")

    ht.display()

    ht.search(3)
    ht.search(6)
    ht.delete(3)
    ht.search(3)

    ht.display()