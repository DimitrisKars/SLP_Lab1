import sys

class TrieNode:
    def __init__(self):
        self.fst_state = None
        self.children = {}


def insert_word(node, word, next_state):
    """
    Inserts a word into the Trie, creating FST states for each TrieNode.

    Args:
    node (TrieNode): The current TrieNode.
    word (str): The remaining part of the word being inserted.
    next_state (int): The next available FST state ID.
    """

    if not word:
        node.fst_state = next_state[0]
        next_state[0] += 1
        return

    c = word[0]
    if c not in node.children:
        node.children[c] = TrieNode()

    insert_word(node.children[c], word[1:], next_state)


def trie_to_fst(node, parent_state, edge_label, arcs):
    """
    Converts Trie to FST by creating transitions in the FST for each edge in the Trie.

    Args:
    node (TrieNode): The current TrieNode.
    parent_state (int): The FST state ID corresponding to the parent TrieNode.
    edge_label (str): The edge label between the parent and the current TrieNode.
    arcs (list): A list of arcs in the FST represented as tuples (from_state, to_state, label).
    """

    if parent_state is not None:
        arc = (parent_state, node.fst_state, edge_label)
        arcs.append(arc)

    for label, child in node.children.items():
        trie_to_fst(child, node.fst_state, label, arcs)


def main():
	f=open("words_only.syms","a")
	dictionary=f.read()
    # Read the dictionary (one word per line) from stdin
    #dictionary = [line.strip() for line in "words_only.syms"]

    # Create the Trie
    root = TrieNode()
    next_state = [0]

    for word in dictionary:
	print(word)
        insert_word(root, word, next_state)

    # Convert Trie to FST
    arcs = []
    final_states = set()
    for label, child in root.children.items():
        trie_to_fst(child, root.fst_state, label, arcs)
        if child.children == {}:
            final_states.add(child.fst_state)

    # Write the FST to a text file in the AT&T format
    with open("fst.att", "w") as f:
        for from_state, to_state, label in arcs:
            f.write(f"{from_state} {to_state} {label} {label}\n")
        for final_state in final_states:
            f.write(f"{final_state}\n")


if __name__ == "__main__":
    main()
