def urlify(string, length):
    url_string = [None] * len(string)
    counter = 0
    for i in range(0, length):
        char = string[i]
        if char != ' ':
            url_string[counter] = char
            counter += 1
        else:
            url_string[counter] = '%'
            url_string[counter + 1] = '2'
            url_string[counter + 2] = '0'
            counter += 3
    return url_string


print(urlify(['h', 'i', ' ', 'b', 'o', 'b', ' ', '!', ' ', ' ', ' ', ' '], 8))