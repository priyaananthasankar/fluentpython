class Node:
    def __init__(self, prev=None, next=None,data=0):
        self.prev = prev
        self.next = next
        self.data = data

# Basically build a hashmap where value of each key directly points to a doubly linked list.
# That way you are able to do both get and put in O(1)
# Easy way is to use OrderedDict in Python collections
class LRUCache:

    def __init__(self,capacity):
        self.capacity = capacity
        self.map = {}
        self.head = Node()
        self.tail = self.head
        
    def get(self,key):
        try:
            current_node = self.map[key]

            # move this node to head, adjust other nodes
            current_node.prev.next = current_node.next
            current_node.prev = None
            current_node.next = self.head
            self.head.prev = current_node
            self.head = current_node

            # return data
            return current_node.data
        except KeyError:
            return -1

    def put(self,key,value):

        # if map is empty, then populate tail
        if len(self.map) == 0:
            self.head.data = value
            self.map[key] = self.head
            return
        elif len(self.map) == self.capacity:
            # evict
            tmp_node = self.tail
            self.tail = self.tail.prev
            self.tail.next = None

            # garbage collect and go into void
            tmp_node.next = None
            tmp_node.prev = None

        # create a new node and attach it to the map
        newnode = Node(None, None,value)
        self.map[key] = newnode

        # adjust the newnode as head of the DLL
        newnode.next = self.head
        self.head.prev = newnode
        self.head = newnode

cache = LRUCache(4)

# key does not exist
print(cache.get(1))

# Put a bunch of keys till it fills cache capacity
cache.put(2,2)
cache.put(3,3)
cache.put(4,4)
cache.put(5,5)
cache.put(2,2)

# Ask for the same key again - watch it move to head
print(cache.get(4))
print("Success")

            

        


