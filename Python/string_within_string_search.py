# write a function that accepts two strings as arguments
# and returns True if either string occurs anywhere in the other
# else return False

a = input('Enter a word:')
b = input('Enter another word:')


def word_in_word(word_a, word_b):
    found = False
    for i in range(len(word_a)):
        substr = word_a[i:i + len(word_b)]
        print(substr)
        if word_b == substr:
            found = True
            break
    if found:
        print('found the string')
    else:
        print('string not found')
    return found


word_in_word(a, b)
