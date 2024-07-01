class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

# Example usage
trie = Trie()
words = ["hello", "world", "hey", "hi", "how"]
for word in words:
    trie.insert(word)

print(trie.search("hello"))  # Output: True
print(trie.search("hey"))    # Output: True
print(trie.search("hi"))     # Output: True
print(trie.search("how"))    # Output: True
print(trie.search("world"))  # Output: True
print(trie.search("bye"))    # Output: False

print(trie.starts_with("hel"))  # Output: True
print(trie.starts_with("wo"))   # Output: True
print(trie.starts_with("heya")) # Output: False
