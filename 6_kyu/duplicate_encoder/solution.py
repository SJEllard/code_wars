def duplicate_encode(word):
    word = word.lower()
    
    count = 0
    dictionary = {}
    new_string = ''
    
    #create dictionary entries
    for i in range(0,len(word)):
        dictionary[word[i]] = 0
         #print(dictionary)

    #count letter apperances 
    for key in dictionary:
        for i in range(0,len(word)):
            if (key == word[i]):
                dictionary[key] += 1 
                #print(dictionary)
                
    #assign replacement value    
    for letter in word:
         if letter in dictionary:
            if dictionary[letter] == 1:
                new_string += '('
            else:
                new_string += ')'
                
    return new_string
    