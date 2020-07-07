from collections import Counter

def is_anagram(s1, s2):
    counter = Counter()
    for c in s1:
        counter[c] += 1
    for c in s2:
        counter[c] -= 1
    
    for i in counter.values():
        if i:
            return False
    return True

def test_is_anagram():
    s1 = "marina"
    s2 = "aniram"
    print(is_anagram(s1, s2))

    s1 = "google"
    s2 = "gouglo"
    print(is_anagram(s1, s2))

if __name__ == "__main__":
    test_is_anagram()