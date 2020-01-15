f = open("zenPython", "r")

w = f.read().split()

words = [i.strip(',.-*! ').lower() for i in w]

print(words[3])
