#SOLUTION, see ipynb for explaination
def last_digit(n, exponent):
    if exponent == 0:
        return 1 
    cycle = [n % 10]
    while True:
        next_num = (cycle[-1] * n) % 10
        if next_num == cycle[0]:
            break
        cycle.append(next_num)
    return cycle[(exponent - 1) % len(cycle)]