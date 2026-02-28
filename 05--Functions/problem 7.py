def rem(l, word):
    while word in l:       # keep removing until no word left
        l.remove(word)
    return l

l = ["Rohan", "an", "Sohabam", "an"]
print(rem(l, "an"))
