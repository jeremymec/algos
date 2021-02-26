from string import ascii_lowercase

def compute_insert_mutations(string):
    mutations = []
    char_array = list(string)

    for i in range(0, len(char_array) - 1):
        for char in ascii_lowercase:
            mutated_char_array = char_array.copy()
            mutated_char_array.insert(i, char)
            mutations.append(''.join(mutated_char_array))

    return mutations

def compute_remove_mutations(string):
    mutations = []
    char_array = list(string)

    for char in char_array:
        mutated_char_array = char_array.copy()
        mutated_char_array.remove(char)
        mutations.append(''.join(mutated_char_array))

    return mutations

def compute_replace_mutations(string):
    mutations = []
    char_array = list(string)

    for i in range(0, len(char_array) - 1):
        for char in ascii_lowercase:
            mutated_char_array = char_array.copy()
            mutated_char_array[i] = char
            mutations.append(''.join(mutated_char_array))

    return mutations

def one_away(first_string, second_string):
    if first_string == second_string:
        return True

    mutations = []
    mutations += compute_insert_mutations(first_string)
    mutations += compute_remove_mutations(first_string)
    mutations += compute_replace_mutations(first_string)

    for mutation in mutations:
        if mutation == second_string:
            return True

    return False

print(one_away("pale", ""))