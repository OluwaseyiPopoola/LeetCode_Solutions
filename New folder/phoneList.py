def main():
    t = int(input())

    for _ in range(t):
        n = int(input())
        trie = TrieNode("*")

        prefix_exist = False
        for _ in range(n):
            phone_no = input()

            if prefix_exist:
                continue
            prefix_exist = trie.add(phone_no)

            
             
        if prefix_exist:
            print("NO")
        else:
            print("YES")
                

            
class TrieNode:
    def __init__(self, val):
        self.val = val
        self.children = {}
        self.end = False

    def add_helper(rootNode, word, i):
        if rootNode.end == True:
            return True
        
        if i == len(word) - 1:
            if word[i] in rootNode.children:
                return True
            
            newNode = TrieNode(word[i])
            rootNode.children[word[i]] = newNode
            newNode.end = True
            return False

        #In a word, letter to be attached is not last letter

        if word[i] in rootNode.children:
            return TrieNode.add_helper(rootNode.children[word[i]], word, i+1)

        newNode = TrieNode(word[i])
        rootNode.children[word[i]] = newNode
        TrieNode.add_helper(newNode, word, i+1)    
        return False

    def add(self, word):
        return TrieNode.add_helper(self, word, 0)
        

        


if __name__ == "__main__":
    main()

"""


  *
  3


"""