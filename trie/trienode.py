class TrieNode:
    ''' A node in trie '''
    def __init__(self, char):
        
        # The character that the node holds
        self.char = char

        # To check whether the word has ended
        self.word_end = False

        # dictionary
        self.child = {}


#if __name__ == "__main__" :
    # trying out the class

