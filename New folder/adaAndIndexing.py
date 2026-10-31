def main():
    n, q = list(map(int, input().split()))
    rootTrie = TrieNode("*")

    for _ in range(n):
        word = input()

        rootTrie.add_child(word)

    for _ in range(q):
        query = input()
        count = rootTrie.count_word_with_prefix(query) if query else n
        print(count) 

    # print(rootTrie)



class TrieNode():
    def __init__(self, val: str):
        self.val = val
        self.end = 0
        self.children = dict() #letter to Node, count
        self.count_words = None

    def add_word_end(self):
        self.end += 1

    def add_child_helper(rootNode:"TrieNode", word: str, i: int):
        letter = word[i]

        nextNode = None
        if letter in rootNode.children:
            nextNode = rootNode.children[letter]
        else:
            newNode = TrieNode(letter)
            rootNode.children[letter] = newNode
            nextNode = newNode

        if i == len(word) - 1:
            nextNode.add_word_end()
            return 

        TrieNode.add_child_helper(nextNode, word, i + 1)



    def add_child(self, word: str):
        TrieNode.add_child_helper(self, word, 0)

    def count_words_hh(rootNode):
        if rootNode.count_words:
            print(rootNode)
            return rootNode.count_words

        count = rootNode.end

        for child in rootNode.children:
            nextNode = rootNode.children[child]
            count += TrieNode.count_words_hh(nextNode)
        

        rootNode.count_words = count
        return rootNode.count_words

    def count_word_with_prefix_helper(rootNode:"TrieNode", query, idx):

        if idx == len(query): 
            rootNode.count_words = TrieNode.count_words_hh(rootNode)
            return rootNode.count_words
            
        letter = query[idx]

        if letter not in rootNode.children:
            return 0  

        nextNode = rootNode.children[letter]
        return TrieNode.count_word_with_prefix_helper(nextNode, query, idx + 1)


    
    def count_word_with_prefix(self, query):
        return TrieNode.count_word_with_prefix_helper(self, query, 0)


    def __repr__(self):
        return f"TrieNode({self.val}, {self.end}, {self.count_words} {self.children})"
        
if __name__ == "__main__":
    main()