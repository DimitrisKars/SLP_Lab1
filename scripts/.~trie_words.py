import sys

class TrieNode:
    """A node in the trie structure"""

    def __init__(self, char):
        # the character stored in this node
        self.char = char

        # whether this can be the end of a word
        self.is_end = False

        # a counter indicating how many times a word is inserted
        # (if this node's is_end is True)
        self.counter = 0

        # a dictionary of child nodes
        # keys are characters, values are nodes
        self.children = {}


class Trie(object):
    """The trie object"""

    def __init__(self):
        self.root = TrieNode("")
        """ The trie has at least the root node. The root node
        does not store any character """
        self.output = []

    def insert(self, word):
        """Insert a word into the trie"""
        node = self.root

        # Loop through each character in the word
        # Check if there is no child containing the character, create a new child for the current node
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                # If a character is not found,
                # create a new node in the trie
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node

        # Mark the end of a word
        node.is_end = True

        # Increment the counter to indicate that we see this word once more
        node.counter += 1

    def dfs(self, node, prefix):
        """Depth-first traversal of the trie

        Args:
            - node: the node to start with
            - prefix: the current prefix, for tracing a
                word while traversing the trie
        """
        if node.is_end:
            self.output.append((prefix + node.char, node.counter))
        
        for child in node.children.values():
            self.dfs(child, prefix + node.char)
        
    def query(self, x):
        """Given an input (a prefix), retrieve all words stored in
        the trie with that prefix, sort the words by the number of 
        times they have been inserted
        """
        # Use a variable within the class to keep all possible outputs
        # As there can be more than one word with such prefix
        self.output = []
        node = self.root
        
        # Check if the prefix is in the trie
        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                # cannot found the prefix, return empty list
                return []
        
        # Traverse the trie to get all candidates
        self.dfs(node, x[:-1])

        # Sort the results in reverse order and return
        return sorted(self.output, key=lambda x: x[1], reverse=True)



def make_input_fst(word):
    """Create an fst that accepts a word letter by letter
    This can be composed with other FSTs, e.g. the spell
    checker to provide an "input" word

    """
    s, accept_state = 0, 10000

    for i, c in enumerate(word):
        # TODO: You need to implement format_arc function in scripts/util
        print(format_arc(s, s + 1, c, c, weight=0))
        s += 1

        if i == len(word) - 1:
            print(format_arc(s, accept_state,"<epsilon>" ," <epsilon>", weight=0))

    print(accept_state)

def format_arc(src, dest, ilabel, olabel, weight):
    return "{} {} {} {} {:.3f}".format(src, dest, ilabel, olabel, weight)



#print(accept_state)



if __name__ == "__main__":
    t=Trie()
    word_list=["aman","big"]
    #with open("words_only.syms", "r") as word_list:
    for word in word_list:
	t.insert(word)
        print(t.dfs(t.root,""))
