def find_anagrams(word,answer,anagrams):
    if word is "":
        anagrams.append(answer)
        return
    for i in range(len(word)):
        ch = word[i]
        left = word[0:i]
        right = word[i+1:]
        rest = left + right
        find_anagrams(rest,answer+ch,anagrams)
anagrams = []
#find_anagrams("abc","",anagrams)
#print(anagrams)
