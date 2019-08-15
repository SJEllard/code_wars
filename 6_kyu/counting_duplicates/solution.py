def duplicate_count(text):
    text = text.lower()
    
    count = 0
    dictionary = {}
    
    #create dictionary keys
    for i in range(0,len(text)):
        dictionary[text[i]] = 0
        #print(dictionary)

    #count unique alphanumerics
    for key in dictionary:
        for i in range(0,len(text)):
            if (key == text[i]):
                dictionary[key] += 1 
                #print(dictionary)
    
    #for every key if key > 1 increase count
    for key in dictionary:
        if dictionary[key] > 1:
            count += 1
        
    return count