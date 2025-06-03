def word_count(book):   # counts the total number of words in the a book
    return len(book.split())

def char_count(book):
    low_book = book.lower()
    count = {}
    for c in low_book:
        if c not in count:
            count[c] = 1
        else:
            count[c] += 1
    return count

def sorted_count(count):
    sc = []
    for c in count:
        if c.isalpha():
            sc.append((c,count[c])) 
    sc.sort(key=lambda x:x[1], reverse=True)
    return sc
