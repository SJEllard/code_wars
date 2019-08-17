def solution(roman):    
    legend = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0 

    while roman:
        #if length of roman is 1 OR dict_name[str_name[0]] greater or equal to dict_name[str_name[1]]
        if len(roman) == 1 or legend[roman[0]] >= legend[roman[1]]:
            #add dict_name[str_name[0]]
            total += legend[roman[0]]
            #update roman
            roman = roman[1:]
        #else (index 0 is less then index 1)
        else:
        #add the difference to the total
            total += legend[roman[1]] - legend[roman[0]]
            #update roman
            roman = roman[2:]
    return total