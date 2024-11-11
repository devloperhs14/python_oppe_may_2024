def check_string_similarity(word: str) -> bool:
    '''
    Given a list of strings, check if all strings follow the formatL
     - where the same word is repeated exactly twice 
     - with a hyphen in-between them. 
     - The word repeated should not be empty.

     Examples of correct format:
     "fast-fast" - correct
     "yeah-yeah" - correct

     "fast-slow" - incorrect (different words)
     "fast-fast-fast" - incorrect (word repeated more than twice)
     "fastfast" - incorrect (no hyphen)
     "asfdadf" - incorrect (no hyphen, word not repeated)
     "-" incorrect (empty word)
    '''

    # split the sentence based on -
    parts = word.split('-')

    # check if split have 2 parts
    has_two_parts = len(parts)==2

    # check if both parts are identical string oe not
    are_parts_identical = parts[0] == parts[1]

    # check if parts are not empty
    is_not_empty = parts[0] != ""

    # combine all conditions
    is_valid = has_two_parts and are_parts_identical and is_not_empty

    # print / return the output
    return is_valid


# test cases
print(check_string_similarity("fast-fast"))       # Expected output: True (correct format, identical words)
print(check_string_similarity("go-go"))           # Expected output: True (correct format, identical words)
print(check_string_similarity("yeah-yeah"))       # Expected output: True (correct format, identical words)

print(check_string_similarity("fast-fast-fast"))  # Expected output: False (incorrect, word repeated more than twice)
print(check_string_similarity("fastfast"))        # Expected output: False (incorrect, no hyphen)
print(check_string_similarity("asfdadf"))         # Expected output: False (incorrect, no hyphen, word not repeated)
print(check_string_similarity("-"))               # Expected output: False (incorrect, empty word)