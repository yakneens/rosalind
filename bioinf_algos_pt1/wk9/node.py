class Trie:
    id = 1
    parentId = 1
    
    maxId = 1
    
    full_string = ""
    
    parent = ""
    value = ""
    children = {}
    
    def __init__(self, value):
        self.value = value 
        self.children = {}       
    
    def addChild(self, new_child):
        self.children[new_child.value] = new_child
        new_child.parentId = self.id
        new_child.parent = self
        Trie.maxId += 1
        new_child.id = new_child.maxId
       
    def getChild(self, value):
        if self.hasChildren():
            return self.children.get(value)
        return None
    
    def addChildrenFrom(self, other_node):
        for child_key in other_node.children:
            other_node.children[child_key].parent = self
            self.children[child_key] = other_node.children[child_key]
    
    def toString(self):
        #return "{0} {1} {2}\n".format(self.parentId,self.id, self.value)
        return "%s %s %s\n" % (self.parentId,self.id, self.value)

    
    def hasChildren(self):
        return self.children != None and len(self.children) > 0
    
    def search(self, my_string):
        cur = self
        for c in my_string:
            for child in cur.children:
                if child.value == c:
                    cur = child
                    break
    
    def initFromStrings(self, string_list):
        f = open('patterns_to_trie.out', 'w')
        for my_string in string_list:
            cur_node = self
            for c in my_string:
                my_match = cur_node.getChild(c)
                if not my_match:
                    new_child = Trie(c)
                    cur_node.addChild(new_child)
                    my_string = new_child.toString()
                    f.write(my_string + "\n")
                    cur_node = new_child
                else:
                    cur_node = my_match
            cur_node.fullString = my_string
            
    