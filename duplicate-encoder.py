def duplicate_encode(word):
    word = word.lower()
    result = ''
    for c in word:
        if word.count(c) == 1:
            result += '('
        else:
            result += ')'
    return result
