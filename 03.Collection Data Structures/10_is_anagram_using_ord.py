import string

def hash_func(astring):
    s = 0
    for one in astring:
        if one in string.whitespace:
            continue
        s = s + ord(one)
    return s

def find_anagram_hash_function(word1, word2):
    return hash_func(word1) == hash_func(word2)

def test_find_anagram_hash_function():
    word1 = "buffy"
    word2 = "bffyu"
    word3 = "bffya"

    print(find_anagram_hash_function(word1, word2))
    print(find_anagram_hash_function(word1, word3))

if __name__ == "__main__":
    test_find_anagram_hash_function()