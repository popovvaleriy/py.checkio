text = "How aresjfhdskfhskd you?"
words = ("how", "are", "you", "hello")

def count_words(text, words):
    t = text.lower()
    l = []
    for i in words:
        m = str(t).count(i)
        if m > 1:
            l.append(m)
        elif m > 0:
            l.append(m)
    return(len(l))

count_words(text, words)
