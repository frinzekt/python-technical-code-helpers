from itertools import permutations, combinations,combinations_with_replacement

# P!
perm = permutations([1, 2, 3])

# NPR
perm2 = permutations([1, 2, 3], 2)

# NCR
comb = combinations([1, 2, 3], 2)

# NCR But With Replacement (meaning you can pick the same item) -->(n+r-1)Cr
combR = combinations_with_replacement([1,2,3],2)

print(list(perm))
print(list(perm2))
print(list(comb))
print(list(combR))