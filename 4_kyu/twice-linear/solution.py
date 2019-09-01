def dbl_linear(n):
    y, z, i, u = 0, 0, 0, [1]
    while i < n:
        next_y, next_z = 2 * u[y] + 1, 3 * u[z] + 1 
        if next_y <= next_z:
            u.append(next_y)
            y += 1
            if next_y == next_z:
                z += 1
        elif next_y >= next_z:
            u.append(next_z)
            z += 1
        i += 1
    return u[n]
    