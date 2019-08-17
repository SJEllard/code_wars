# For building the encrypted string:
# Take every 2nd char from the string, then the other chars, that are not every 2nd char, 
# and concat them as new String.
# Do this n times!

# Examples:

# "This is a test!", 1 -> "hsi  etTi sats!"
# "This is a test!", 2 -> "hsi  etTi sats!" -> "s eT ashi tist!"
# Write two methods:

# def encrypt(text, n)
# def decrypt(encrypted_text, n)
# For both methods:
# If the input-string is null or empty return exactly this value!
# If n is <= 0 then return the input text
############
def encrypt(text, n):
    if n <= 0:
        return(text)
    string = text
    i = 0 
    while i < n:
        letters = [] 
        lead = []
        tail = []
        for l in string:
            letters += l  
        j = 0
        while j < len(letters):
            if j % 2 == 0: 
                #even index 
                tail += letters[j]
            else:  
                #odd index
                lead += letters[j]
            j += 1   
        string = lead + tail
        i += 1
    result = ''
    for l in string:
        result += l
    return(result)

def decrypt(encrypted_text, n):
    if n <= 0:
        return(encrypted_text)
    string = encrypted_text

    #loop decrypt
    i = 0
    while i < n:
        text = list(string)
        length = len(text)
        if length % 2 == 0:
            split = length//2
        else:
            split = (length-1)//2
        lead = text[0:split]
        tail = text[split:length]    
        j = 0 
        result = []
        while j < len(tail):
            result += tail[j]
            if j < len(lead):
                result += lead[j]
            j += 1
        string = ''
        for l in result:
            string += l
        i += 1
    return(string)