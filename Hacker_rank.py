"""

HACKER RANK

def build_coord(x, y, z, n):
    coords = [[i, j, k] for i in range (x+1)
       for j in range (y+1)
       for k in range(z+1)]
    def filter_coord(coord):
       nonlocal n
       return not sum(coord) == n
    coords = list(filter(filter_coord, coords))
    print (coords)
if name
    x = int(input())
    y = int(input ())
    z = int (input ())
    n = int(input())
   build coord(x, y, z, n)
           == '_main__':
"""
y = x = 1
z = 2
n = 3

l1 = [[a, b, c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c != n]

print(l1)


l2 = [(x, y) for x in range(3) for y in range(3) if x != y if (x, y) != (y, x)]

print(l2)