import itertools

def print_permutations(s):
    perms = itertools.permutations(s)
    for perm in perms:
        print("".join(perm))

input = input("Enter a string: ")
print_permutations(input)