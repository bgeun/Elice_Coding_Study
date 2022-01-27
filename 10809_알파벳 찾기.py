word = input()
alphabet = list(range(97,123)) # a-z

for i in alphabet:
  print(word.find(chr(i)))