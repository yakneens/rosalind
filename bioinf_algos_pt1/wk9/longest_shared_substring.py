from suffix_tree import SuffixTree
import cProfile
import re

''' 
myFilename = "/Users/siakhnin/Downloads/dataset_95_5 (2).txt"


f = open(myFilename, 'r')
inputstr = f.read().strip()
f = open('suffix_tree.out', 'w') 
    
'''
inputstr = """TCGGTAGATTGCGCCCACTC$
     AGGGGCTCGCAGTGTAAGAA"""
   
input_list = [x.strip() for x in inputstr.split('\n')]

class LongestSharedSubstringSuffixTree(SuffixTree):    
    
    def findBranch(self, my_string, shared_sub):    
        for child in self.children.values():
            if child.toString()[0] == my_string[0]:
                new_sub = child.traverseBranch(my_string, shared_sub)
                return new_sub
                
        #Did not find a matching child
        return shared_sub
                          
    def traverseBranch(self, my_string, shared_sub):
        my_sub = shared_sub
        
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
                shared_sub = "".join((shared_sub,target_string[:i]))
                return shared_sub
              
        shared_sub = "".join((shared_sub,target_string))
            
        if len(left_over_string) > 0:    
            shared_sub = self.findBranch(left_over_string, shared_sub)
            return shared_sub
        else:
            return shared_sub
            
def doIt():
    my_tree = LongestSharedSubstringSuffixTree((0,0))    
    LongestSharedSubstringSuffixTree.input_string = input_list[0]
    my_tree.initFromStrings(input_list[0][len(input_list[0]) - i - 1:] for i in range(len(input_list[0])))
    
    second_string = input_list[1]
    suffixes = [second_string[len(second_string) - i - 1:] for i in range(len(second_string),0,-1)]
    cur_sub = ""
    max_sub = ""
    
    for suffix in suffixes:
        if len(max_sub) >= len(suffix):
            break
        
        cur_sub = my_tree.findBranch(suffix, "")
        
        if len(cur_sub) > len(max_sub):
            max_sub = cur_sub
    
    print max_sub
doIt()
#cProfile.run('doIt()')    