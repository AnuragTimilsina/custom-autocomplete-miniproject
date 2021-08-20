class TrieNode:
    ''' A node in trie '''
    def __init__(self, char):
        
        # The character that the node holds
        self.value = char

        # To check whether the word has ended
        self.stop = False

        # dictionary
        self.children = {}


#if __name__ == "__main__" :
    # trying out the class

