def productFib(n):
    #iterative solution
    a = [0, 1]
    i = 3 
    while i <= n:
        if a[0] * a[1] == n:
            array = [a[0], a[1], True]
            return array
        elif a[0] * a[1] > n:
            array = [a[0], a[1], False]
            return array
        else:
            new = a[0] + a[1]
            a[0] = a[1]
            a[1] = new
            i += 1