class Trie:

    def __init__(self):
        self.wordlist = []

    def insert(self, word: str) -> None:
        self.wordlist.append(word)

    def search(self, word: str) -> bool:
        return word in self.wordlist

    def startsWith(self, prefix: str) -> bool:
        n = len(prefix)
        for i in range(len(self.wordlist)):
            if self.wordlist[i][0:n] == prefix:
                return True
        return False
    
class Trie1:

    def __init__(self):
        self.root={}
        
    def insert(self, word: str) -> None:

        cur=self.root

        for letter in word:
            if letter not in cur:
                cur[letter]={}
            cur=cur[letter]

        cur['*']=''

    def search(self, word: str) -> bool:

        cur=self.root
        for letter in word:
            if letter not in cur:
                return False
            cur=cur[letter]

        return '*' in cur
        
    def startsWith(self, prefix: str) -> bool:

        cur=self.root
        for letter in prefix:
            if letter not in cur:
                return False
            cur=cur[letter]

        return True
    
obj = Trie1()
obj.insert("apple")
obj.search("apple")
obj.search("app")
obj.startsWith("app")
obj.insert("app")
obj.search("app")