f = open("zenPython", "r")

w = f.read().split()

words = [i.strip(',.-*! ').lower() for i in w]

word_frequency = {x:words.count(x) for x in words}

print(word_frequency['the'])
