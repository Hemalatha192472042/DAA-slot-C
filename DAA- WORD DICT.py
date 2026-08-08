class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False


class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        current = self.root

        for char in word:
            if char not in current.children:
                current.children[char] = TrieNode()

            current = current.children[char]

        current.end = True

    def search(self, word):
        def dfs(node, index):
            if index == len(word):
                return node.end

            char = word[index]

            if char == '.':
                for child in node.children.values():
                    if dfs(child, index + 1):
                        return True
                return False

            if char not in node.children:
                return False

            return dfs(node.children[char], index + 1)

        return dfs(self.root, 0)


dictionary = WordDictionary()

dictionary.add_word("bad")
dictionary.add_word("dad")
dictionary.add_word("mad")

print(dictionary.search("bad"))
print(dictionary.search("pad"))
print(dictionary.search(".ad"))
print(dictionary.search("b.."))
