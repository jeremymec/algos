
def compute_permutations(current, remaining, permutations):

    if len(remaining) <= 0:
        permutations.append(current)
    
    for char in remaining:
        new_current = current.copy()
        new_remaining = remaining.copy()
        new_current.append(char)
        new_remaining.remove(char)
        compute_permutations(new_current, new_remaining, permutations)
    
    return permutations

def is_palindrome(string_array):

    backwards_string_array = []
    for char in string_array:
        backwards_string_array.insert(0, char)
    return string_array == backwards_string_array

def is_palindrome_2(string_array):
    i = 0
    j = len(string_array) - 1

    while (i < j):
        if string_array[i] != string_array[j]:
            return False
        i = i + 1
        j = j - 1

    return True


def is_palindrome_permutation(string):

    permutations = compute_permutations([], list(string), [])
    for permutation in permutations:
        if ' ' in permutation:
            permutation.remove(' ')
        if is_palindrome_2(permutation):
            print('Palindrome found, ', permutation)
            return True

    return False

print(is_palindrome_permutation('tact coa'))
