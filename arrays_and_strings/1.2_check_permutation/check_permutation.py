
def check_permutation(string_one="ac", string_two="ca"):
    perms_one = compute_permutation([], list(string_one), [])
    perms_two = compute_permutation([], list(string_two), [])
    for perm_one in perms_one:
        for perm_two in perms_two:
            if perm_one == perm_two:
                print("Permutation found, ", perm_one)
    
def compute_permutation(current, remaining, perms):
    if remaining == []:
        perms.append(current)
    for element in remaining:
        n_remaining = list(remaining)
        n_remaining.remove(element)
        n_current = list(current)
        n_current.append(element)
        compute_permutation(n_current, n_remaining, perms)
    return perms

check_permutation()