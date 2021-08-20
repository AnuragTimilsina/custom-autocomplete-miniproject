from trie import Trie

t = Trie()
t.insert("furniture")
t.insert("future")
t.insert("anurag")
t.insert("anuragdon")
print(t.query("fu"))
print(t.query("anu"))