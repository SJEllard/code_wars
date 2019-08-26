def perimeter(n):
    if n == 0:
        return 4
    elif n == 1:
        return 8
    else:
        i = 0
        last_two = [1, 1]
        result = 2
        while i < (n-1):
            nextside = sum(last_two)
            last_two[0] = last_two[1]
            last_two[1] = nextside
            result += (nextside )
            i += 1
        return (result*4)  