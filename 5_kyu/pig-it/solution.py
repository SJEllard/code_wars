def pig_it(text):
    result = ''
    words = text.split(" ")
    for word in words:
        if word != "!" and word != "?":
            suffix_one = word[0]
            suffix_two = "ay"
            word = word[1 : : ] + suffix_one + suffix_two
        if result == "":
            result += word
        else:
            result += " " + word
    return result