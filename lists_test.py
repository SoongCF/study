# 序列
s = [1, 2, 3, 4, 5]
print(s)
print(s[0])
print(s[4])
print(s[0:3])
print(s[-2:])

s += [11, 12, 13]
print(s[:])

s[4] = 10
print(s)

s.append(14)
print(s)



letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(letters)
letters[3:6] = ['D', 'E', 'F']
print(letters)
letters[2:4] = []
print(letters)

letters_len = len(letters)
print(letters_len)




a = [1, 2, 3]
b = ['a', 'b']
x = [a, b]
print(a)
print(b)
print(x)
print(x[0])
print(x[1])
print(x[0][1])
print(len(x))
print(len(x[0]))
print(len(x[1]))
