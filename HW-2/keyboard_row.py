from collections import defaultdict


def keyboard_row(words_lst):
  dic = defaultdict(set) #O(n)

  for word in words_lst: #O(n)
    for letter in word: #O(n)
      if letter.lower() in "qwertyuiop": #O(1)
        dic[word].add(1)
      elif letter.lower() in "asdfghjkl": #O(1)
        dic[word].add(2)
      elif letter.lower() in "zxcvbnm": #O(1)
        dic[word].add(3)
    if len(dic[word]) > 1: 
      dic.pop(word) #O(1)
  return set(dic.keys())


print(keyboard_row(["hello", "alaska", "dad", "peace"]))
