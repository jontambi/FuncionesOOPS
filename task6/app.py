f = open("zenPython", "r")

w = f.read().split()

words = [i.strip(',.-*! ').lower() for i in w]

word_frequency = {x:words.count(x) for x in words}

frequent_words = {k:y for (k, y) in word_frequency.items() if y > 5}

print(frequent_words)

print(len(frequent_words))