#function to check whether first and second characters of words match
def match_word(words):
    ctr = 0
    lst = []
    for word in words:
        if len(word) > 1 and word[0] == word[-1]:
            ctr += 1
            lst.append(word)
    print("list of words with first and last character same\n",lst)
    return ctr
count = match_word(['abc','cfc','xyz','aba','1221'])
print("nomber of words having first and last character same:",count)