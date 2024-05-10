class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        self.hash_map = [Node(0, 0) for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        index = key % len(self.hash_map)
        cur = self.hash_map[index]

        while cur.next != None:
            if cur.next.key == key:
                cur.next.val = value
                return

            cur = cur.next
        
        cur.next = Node(key, value)

    def get(self, key: int) -> int:
        index = key % len(self.hash_map)
        cur = self.hash_map[index]

        while cur.next != None:
            if cur.next.key == key:
                return cur.next.val
            
            cur = cur.next

        return -1

    def remove(self, key: int) -> None:
        index = key % len(self.hash_map)
        cur = self.hash_map[index]

        while cur.next != None:
            if cur.next.key == key:
                cur.next = cur.next.next
                return

            cur = cur.next
        
        return -1

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)