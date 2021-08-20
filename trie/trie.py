from trie.trienode import TrieNode

class Trie(object):

    def __init__(self):

        # The root node:
        self.root = TrieNode("")
        print("Constructor called!!!\n")

    def insert(self, word):
        ''' insert word in trie '''

        node = self.root

        for char in word:
            # If child of similar letter exists
            # Then just move on! 
            if char in node.children:
                node = node.children[char]
            # If there's no child that contains that char,
            # Create a new child node 
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        
        node.stop = True

    def traverse(self, node, prefix):
        ''' DFS for trie: 

            node: starting node
            prefix: semi_complete word for tracing possible words
        '''
        if node.stop:
            self.output_words.append((prefix + node.value))
        for c in node.children.values():
            self.traverse(c, prefix + node.value)

    def query(self, x):
        '''
            Retrive all the words stored in the trie
            with given prefix. Sort the words by the
            number of times they have been inserted.
        '''

        self.output_words = [] # list of possible words
        node = self.root


        for char in x:
            if char in node.children:
                node = node.children[char]
            else:
                return[] # If word not found

        # Traverse the trie to get all candidates
        self.traverse(node, x[:-1])

        #Sort the results and return
        return sorted(self.output_words)
