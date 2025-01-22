# simple pointer method and a circle queue such as ["hello", "world"] fill in a screen.
# ["hello" "world" "hello"] ["world" "hello" "world"]
# image there is a pointer go around the string. And we need add a space behind the string.
# "hello" "world" ->"hello" "world" "hello" "world" "hello" "world"
# move forward the pointer by the length of row every time
# If the pointer point at a space, then we can move forward by one.
# If the pinter point at the end of a word then move forward by 2.
# If the pointer point a letter, then move backward until the space.

class Solution(object):
  def wordsTyping(self, sentence, rows, cols):
    """
    :type sentence: List[str]
    :type rows: int
    :type cols: int
    :rtype: int
    """
    pointer = 0
    string = " ".join(sentence) + " "
    n = len(string)
    i = 0
    while i < rows:
      pointer += cols - 1
      if string[pointer % n] == " ":
        pointer += 1
      elif string[(pointer + 1) % n] == " ":
        pointer += 2
      else:
        while pointer > 0 and string[(pointer - 1) % n] != " ":
          pointer -= 1
      i += 1
    return pointer//n

solution = Solution()
print(solution.wordsTyping(rows = 2, cols = 8, sentence = ["hello", "world"]))
print(solution.wordsTyping(rows = 3, cols = 6, sentence = ["a", "bcd", "e"]))
print(solution.wordsTyping(rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]))