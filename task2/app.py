f = open("zenPython", "r")

w = f.read().split()

words = []
for i in w:
    words.append(i.strip(',.-*! '))


print(words[3])
