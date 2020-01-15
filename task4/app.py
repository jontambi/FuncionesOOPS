f = open("zenPython", "r")

w = f.read().split()

def unique(w):
    words = [i.strip(',.-*! ').lower() for i in w]
    unique_words = set(words)
    print(len(unique_words))


unique(w)
