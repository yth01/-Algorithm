n = int(input())

stars = [[' '] * (2*n) for _ in range(n)]


def recursion(r, c, size):
    if size == 3:
        stars[r][c] = '*'
        stars[r+1][c-1] = '*'
        stars[r+1][c+1] = '*'
        for i in range(-2, 3):
            stars[r+2][c-i] = '*'    
    else:
        div_size = size // 2
        recursion(r, c, div_size)
        recursion(r + div_size, c - div_size, div_size)
        recursion(r + div_size, c + div_size, div_size)


recursion(0, n-1, n)
for star in stars:
    print(''.join(star))
