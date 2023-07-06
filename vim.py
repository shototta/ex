n = str("всем привет я я я я всем привет на тебе")
print(f' кол-во слов : {n.count(" ")+1}')
n = n.lower()
n = n.split(" ")
d = {}
for element in n:
    if element in d:
        d[element] += 1
    else:
        d[element] = 1
for element, count in d.items():
    print(element, count)

