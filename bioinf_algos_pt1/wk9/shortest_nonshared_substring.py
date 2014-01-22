from node import Trie
import cProfile
import re


myFilename = "/Users/siakhnin/Downloads/dataset_95_6 (1).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
f = open('suffix_tree.out', 'w') 
    
'''

inputstr = """CAAGT
     CAGT$"""
inputstr = """CTGCTT
     AGTGCTGGGCTGGCT"""
inputstr = """CCAAGCTGCTAGAGG
     CATGCTGGGCTGGCT"""
'''   
input_list = [x.strip() for x in inputstr.split('\n')]

class SuffixTree(Trie):
    input_string = ""
    offset = 0
    sub_length = 0

    def toString(self):
        return SuffixTree.input_string[self.value[0]:sum(self.value)]


    def findSplitBranch(self, my_string, my_string_offset):    
        # Find the child of self that starts with the same letter as my_string
        # that will be the branch my_string needs to be inserted into
        for child in self.children.values():
            if child.toString()[0] == my_string[0]:
                #Insert my_string at this child as they share a prefix
                child.insert(my_string, my_string_offset)
                return                
        
        #If no children are found that share a prefix with my_string it is inserted as a child of self
        new_child = SuffixTree((my_string_offset,len(my_string)))
        new_child.full_string = my_string
        self.addChild(new_child)
       
    
    def insert(self, my_string, my_string_offset):
        
        cur_node = self
        
        #The string we are trying insert
        target_string = my_string
        target_string_len = len(target_string)
        
        #String represented by the current node
        cur_string = cur_node.toString()
        cur_string_len = len(cur_string)
        
        # Need to compare strings of the same size
        # If no divergence found on this segment will need to check
        # the left_over_string against one of the children
        left_over_string = ""
        if target_string_len > cur_string_len: 
            left_over_string = target_string[cur_string_len:]
            target_string = target_string[:cur_string_len]
            
        #Compare the first target_string_len characters, if a difference
        # is found that becomes the split point
        split_point = 0
        for i,c in enumerate(target_string):
            if c != cur_string[i]:
                split_point = i
                break
            split_point = cur_string_len
     
        if split_point > 0:
            #Need to split here
            if split_point < cur_string_len:
                
                #The split consists of splitting the current node at the split_point
                #As a result cur_node represents the common substring, new_child
                #represents the remainder of cur_node, and other_child represents
                #the remainder of target_string
                cur_node.value = (cur_node.value[0], split_point)
                cur_node.full_string = cur_node.toString()
                
                #New_child takes over the children of cur_node
                new_child = SuffixTree((cur_node.value[0] + split_point, len(cur_string) - split_point))
                new_child.addChildrenFrom(cur_node)
                #new_child.children = cur_node.children
                new_child.full_string = new_child.toString()
                
                
                other_child = SuffixTree((my_string_offset + split_point, len(my_string) - split_point))
                other_child.full_string = other_child.toString()
            
                #new_child and other_child become the new children of cur_node
                cur_node.children = {}
                cur_node.addChild(new_child)
                cur_node.addChild(other_child)
                return
            
            #This is the case where no divergence was found between target_string and cur_node
            #Need to explore the children of cur_node to examine for divergence.
            else:
                self.findSplitBranch(left_over_string, my_string_offset + split_point)
                   
    def initFromStrings(self, string_list):
            for my_string in string_list:
                self.findSplitBranch(my_string, len(SuffixTree.input_string) - len(my_string))
            
    def printNodes(self):
        if not self.hasChildren():
            return
        else:
            for child in self.children.values():
                #f.write(child.toString() + "\n")  
                print(child.toString() + "\n")         
                child.printNodes()
    
    def findBranch(self, my_string):    
        for child in self.children.values():
            if child.toString()[0] == my_string[0]:
                return child.traverseBranch(my_string)
                
        #Did not find a matching child
        return my_string[0]
                          
    def traverseBranch(self, my_string):
        cur_node = self
        
        target_string = my_string
        target_string_len = len(target_string)
        
        #String represented by the current node
        cur_string = cur_node.toString()
        cur_string_len = len(cur_string)
        
        # Need to compare strings of the same size
        # If no divergence found on this segment will need to check
        # the left_over_string against one of the children
        left_over_string = ""
        if target_string_len > cur_string_len: 
            left_over_string = target_string[cur_string_len:]
            target_string = target_string[:cur_string_len]
            target_string_len = len(target_string)
            
        #Compare the first target_string_len characters, if a difference
        # is found that becomes the split point
        for i,c in enumerate(target_string):
            if c != cur_string[i]:
                #compute common substring here
                return cur_string[:i] + target_string[i]
              
        if len(left_over_string) > 0:
            my_result = self.findBranch(left_over_string)
            if len(my_result) > 0:
                return cur_string + my_result
        
        return ""
        
        
            
def doIt():
    my_tree = SuffixTree((0,0))
    first_string = input_list[1] + "$"    
    SuffixTree.input_string = first_string
    my_tree.initFromStrings(first_string[len(first_string) - i - 1:] for i in range(len(first_string)))
    
    second_string = input_list[0]
    suffixes = [second_string[len(second_string) - i - 1:] for i in range(len(second_string),0,-1)]
    cur_sub = ""
    shortest = ""
    
    for suffix in suffixes:
        
        cur_sub = my_tree.findBranch(suffix)
        
        if  shortest == "" or (cur_sub != "" and len(cur_sub) < len(shortest)):
            shortest = cur_sub
    
    
    print shortest
    
doIt()
#cProfile.run('doIt()')    