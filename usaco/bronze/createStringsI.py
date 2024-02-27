"""
  Permutations problem (easy)
  Given a string, print all permutations of the string
"""

n = input()

def permutations(generated_perms, current_perm, elementsToPerm):
  elementsToPermSorted = ''.join(sorted(elementsToPerm))
  if len(elementsToPerm) > 0:
    for i in range(len(elementsToPermSorted)):
      element = elementsToPermSorted[i]
      next_perm = current_perm+element
      remaining_elements = elementsToPermSorted[:i]+elementsToPermSorted[i+1:]

      permutations(generated_perms, next_perm, remaining_elements)
  else:
    generated_perms.append(current_perm)

  return generated_perms


results = set(permutations([], '', n))

print(len(results))
for element in results:
  print(element)