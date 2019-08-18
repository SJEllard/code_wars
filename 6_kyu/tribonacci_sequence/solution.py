def tribonacci(signature, n):
    if n == 0: 
        return []
    elif n == 1:
        return [signature[0]]
    elif n == 2:
        return [signature[0], signature[1]]
    else:
        result = list(signature)
        heap = list(signature)
        count = n - 3
        i = 0
        while i < count:
            nextnum = sum(heap)
            heap.pop(0), heap.append(nextnum), result.append(nextnum)
            i += 1
        return result
