n = int(input())
s = ''
j = 1
k = 0
razm = 0

for i in range(1, n + 1):
    if k < j:
        k += 1
        if k != j:
            s = s + str(i) + ' '
        else:
            s = s + str(i)
            if len(s) > razm:
                razm = len(s)
            s = ''
            k = 0
            j += 1
if s != '':
    if len(s) > razm:
        razm = len(s)
    
s = ''
j = 1
k = 0

for i in range(1, n + 1):
    if k < j:
        k += 1
        if k != j:
            s = s + str(i) + ' '
        else:
            s = s + str(i)
            print(s.center(razm))
            s = ''
            k = 0
            j += 1
if s != '':
    print(s.center(razm))