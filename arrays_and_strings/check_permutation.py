# def check_permutation(stringe_one="banana", string_two="apple"):

def compute_permutation(current, remaining):
    if remaining == []:
        print(current)
    for element in remaining:
        n_remaining = list(remaining)
        n_remaining.remove(element)
        n_current = list(current)
        n_current.append(element)
        compute_permutation(n_current, n_remaining)

compute_permutation([], [1, 2, 3])
