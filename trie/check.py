from trie import Trie

t = Trie()

#checking insertion: 
t.insert("furniture")
t.insert("fusion")
t.insert("future")
t.insert("anurag")
t.insert("anuragdon")

#checking query:
print(t.query("fu"))
print(t.query("anu"))

#Checking remove:
t.remove("furniture")
print(t.query("fu"))

t.remove("fusion")
print(t.query("fu"))