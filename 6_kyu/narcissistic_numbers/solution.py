def narcissistic(value):
    #make an array of each digit in the value
    digits = [int(d) for d in str(value)]
    total = 0
    
    #augment each digit and add to total
    for d in digits:
        if d == 1:
            total += 1
            print(d)
        else:
            d = d**len(digits)
            total += d
            print(d)
        
    #compare total to value
    if total == value:
        return True
    else:
        return False