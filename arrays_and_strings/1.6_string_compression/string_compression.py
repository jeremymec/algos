def compress_string(string):
    compressed_char_array = []
    char_array = list(string)

    count = 1

    for i, char in enumerate(char_array):
        if i == len(char_array) - 1:
            compressed_char_array.append(char)
            compressed_char_array.append(str(count))
            break
        if char == char_array[i + 1]:
            count += 1
        else:
            compressed_char_array.append(char)
            compressed_char_array.append(str(count))
            count = 1
    
    return ''.join(compressed_char_array)

print(compress_string("aabcccccaaa"))