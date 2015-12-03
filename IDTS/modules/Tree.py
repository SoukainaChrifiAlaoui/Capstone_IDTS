class Node:
    #Node Constructor
    def __init__(self, key, data):
        self.left = None
        self.right = None
        self.data = data
        self.key = key
        self.parent = None
        self.hint = None
    #set parent of a node
    def set_parent (self, parent):
        self.parent = parent
    #set the root of the tree
    def is_root(self):
        self.parent = Node (0, "")
    #get hint embedded in the node
    def get_hint (self):
        str = "%s" % (self.hint)
        return str

    #print one node
    def print_node (self):
        str = "key: %d  AND data: %s AND parent: %s" % (self.key, self.data, self.parent.data)
        print (str)
    #insert new nodes in the tree
    def insert (self, key, data):
        if (self.key):
            if key < self.key:
                if self.left is None:
                    self.left = Node (key, data)
                else:
                    self.left.insert (key, data)
            elif key > self.key:
                if self.right is None:
                    self.right = Node(key, data)
                else:
                    self.right.insert(key, data)
        else:
            self.data = data
    #check if node is a leaf
    def isLeaf(self):
        return not (self.right or self.left)
    #print tree
    def print (self):
        print (self.data)
        if self.left:
            self.left.print()
        if self.right:
            self.right.print()
    #set the key for a node
    def attribute_key (self, data):
        key = 0
        if data == '1':
            key = 26
        elif data == '2':
            key = 24
        elif data == '3':
            key = 18
        elif data == '4':
            key = 11
        elif data == '5':
            key = 4
        return key
    #search for a node in the tree
    def search (self, data, parent=None):
        key = self.attribute_key(data)
        if key < self.key:
            if self.left is None:
                return None
            return self.left.search(data,self)
        elif key > self.key:
            if self.right is None:
                return None
            return self.right.search(data,self)
        else:
            return self
    #find youngest common ancestor
    def findAncestor (self, data_ans, data_sol ):
        visited = set()
        answer_node = self.search(data_ans)
        sol_node = self.search(data_sol)

        if sol_node.key==answer_node.key:
            return sol_node
        while sol_node.key != answer_node.key:
            sol_node = sol_node.parent
            answer_node = answer_node.parent
        return sol_node
