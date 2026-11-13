# 1. Hash Table
class HashTable:
    def __init__(self):
        self.data = {}

    def add_suburb(self, name):
        if name not in self.data:
            self.data[name] = []
            print(f"[Hash Table] Added suburb: {name}")

    def find_suburb(self, name):
        if name in self.data:
            print(f"[Hash Table] Found '{name}' in index.")
            return True
        print(f"[Hash Table] '{name}' was not found.")
        return False


# 2. Binary Search Tree
class Node:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def add_suburb(self, name):
        if self.root is None:
            self.root = Node(name)
            print(f"[BST] Added root suburb: {name}")
        else:
            self.insert(self.root, name)

    def insert(self, current, name):
        if name < current.name:
            if current.left is None:
                current.left = Node(name)
                print(f"[BST] Added suburb: {name}")
            else:
                self.insert(current.left, name)
        elif name > current.name:
            if current.right is None:
                current.right = Node(name)
                print(f"[BST] Added suburb: {name}")
            else:
                self.insert(current.right, name)

    def find_suburb(self, name):
        return self.search(self.root, name)

    def search(self, current, name):
        if current is None:
            print(f"[BST] '{name}' was not found.")
            return False
        if name == current.name:
            print(f"[BST] Found '{name}' in tree.")
            return True
        elif name < current.name:
            return self.search(current.left, name)
        else:
            return self.search(current.right, name)


# Demo
suburbs = [
    "Oakridge", "Bellville", "Wynberg", "Claremont",
    "Rondebosch", "Sea Point", "Newlands", "Goodwood"
]

print("--- Populating Hash Table (8 Suburbs) ---")
hash_table = HashTable()
for item in suburbs:
    hash_table.add_suburb(item)

print("\n--- Populating Binary Search Tree (8 Suburbs) ---")
bst_tree = BST()
for item in suburbs:
    bst_tree.add_suburb(item)

print("\n--- Testing Find Operation on Both Structures ---")
hash_table.find_suburb("Claremont")
hash_table.find_suburb("Midrand")

bst_tree.find_suburb("Claremont")
bst_tree.find_suburb("Midrand")



# Alphabetical Listing
def list_suburbs_in_order(start_node, all_names=None):
    if all_names is None:
        all_names = []

    if start_node is not None:
        list_suburbs_in_order(start_node.left, all_names)
        all_names.append(start_node.name)
        list_suburbs_in_order(start_node.right, all_names)

    return all_names

print("\n--- 4.2 Alphabetical Suburb List (from BST) ---")
result = list_suburbs_in_order(bst_tree.root)
for number, name in enumerate(result, start=1):
    print(f"{number}. {name}")



# Maintaining Incident Counts per Suburb
class SimpleIncidentTracker:
    def __init__(self):
        self.counts = {}

    def add_suburb(self, name):
        if name not in self.counts:
            self.counts[name] = 0

    def add_incident(self, name):
        if name not in self.counts:
            self.counts[name] = 0
        self.counts[name] += 1
        print(f"[INCIDENT LOGGED] {name} now has {self.counts[name]} incident(s).")

    def get_count(self, name):
        total = self.counts.get(name, 0)
        print(f"[REPORT] {name}: {total} recorded incident(s).")
        return total


print("\n--- 4.3 Suburb Incident Counter Demonstration ---")
tracker = SimpleIncidentTracker()

for place in ["Bellville", "Claremont", "Wynberg"]:
    tracker.add_suburb(place)

tracker.add_incident("Bellville")
tracker.add_incident("Claremont")
tracker.add_incident("Bellville")
tracker.add_incident("Bellville")

print("\n--- Suburb Incident Summary ---")
tracker.get_count("Bellville")
tracker.get_count("Claremont")
tracker.get_count("Wynberg")