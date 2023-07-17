def one_edit_away(s1, s2):
  counter = 0;
  for letter in s1:
    if not(letter in s2):
      counter += 1
  return counter < 2