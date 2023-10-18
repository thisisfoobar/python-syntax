def print_upper_words(words,must_start_with):
    '''loop through list of words and print out each word in all caps'''
    for word in words:
        for start in must_start_with:
            start_len = len(start)
            if start.upper() == word[0:start_len].upper():
                print(word.upper())

print_upper_words(["hello","howdy","goodbye","telephone","beanie"], {"hE","b"})
