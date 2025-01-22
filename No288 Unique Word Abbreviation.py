from collections import defaultdict
from typing import List
class ValidWordAbbr:
    def __init__(self, dictionary: List[str]):
        self.words = defaultdict(set)
        for word in dictionary:
            key = self.wordabbr(word)
            self.words[key].add(word)

    def isUnique(self, word: str) -> bool:
        key = self.wordabbr(word)
        if key not in self.words.keys():
            return True
        else:
            if len(self.words[key]) == 1 and word in self.words[key]:
                return True 
        return False
    
    def wordabbr(self, word):
            if len(word) > 2:
                key = word[0] + str(len(word) - 2) + word[-1]
            else:
                key = word
            return key
    # def word_abbr(self, s):
    #     return s if len(s) < 3 else f'{s[0]}{len(s) - 2}{s[-1]}'

validWordAbbr = ValidWordAbbr(["deer", "door", "cake", "card"])
print(validWordAbbr.isUnique("dear")) # return false, dictionary word "deer" and word "dear" have the same abbreviation "d2r" but are not the same.
print(validWordAbbr.isUnique("cart")) # return true, no words in the dictionary have the abbreviation "c2t".
print(validWordAbbr.isUnique("cane")) # return false, dictionary word "cake" and word "cane" have the same abbreviation  "c2e" but are not the same.
print(validWordAbbr.isUnique("make")) # return true, no words in the dictionary have the abbreviation "m2e".
print(validWordAbbr.isUnique("cake")) # return true, because "cake" is already in the dictionary and no other word in the dictionary has "c2e" abbreviation.