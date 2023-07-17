import math
from collections import defaultdict


def most_common_word(s):
  dic = defaultdict(int) #O(n)
  max_count = -math.inf
  max_word = ""

  for word in s.split():  #O(n)
    dic[word] += 1  #O(1)
    if (dic[word] > max_count): #O(1)
      max_word = word
      max_count = dic[word]  #O(1)
  return max_word


print(most_common_word("hello world hello hello world hi"))
