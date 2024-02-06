"""
Block game

Simulation (USACO) - medium
http://www.usaco.org/index.php?page=viewproblem2&cpid=664
"""
fin = open('blocks.in', 'r')
fout = open('blocks.out', 'w')

def encode(word):
  encoded = [0]*26
  for letter in word:
    encoded[ord(letter)-97] += 1

  return encoded

def get_letters_by_card(word1, word2):
  word1_encoded = encode(word1)
  word2_encoded = encode(word2)
  return [max(word1_encoded[i], word2_encoded[i]) for i in range(26)]


# Read the input

n = int(fin.readline())

letters = [0]*26
for _ in range(n):
  word1, word2 = [x for x in fin.readline().rstrip().split(' ')]
  card_letters = get_letters_by_card(word1, word2)

  for i in range(26):
    letters[i] += card_letters[i]


# Save the output

for letter in letters:
  fout.write(f'{letter}\n')
