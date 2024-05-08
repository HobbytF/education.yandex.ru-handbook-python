n = int(input())
n1 = n
new = 0
while (o := n1 % 10) != 0:
    new = new * 10 + o
    n1 = n1 // 10
print('n   =', n)
print('new =', new)
if n == new:
    print("YES")
else:
    print("NO")