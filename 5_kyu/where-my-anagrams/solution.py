def anagrams(word, words):
#return word for word in words in sorted lowercase word == sorted lowercase word
    return [w for w in words if sorted(w.lower()) == sorted(word)]