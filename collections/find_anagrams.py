def find_anagrams(word,answer):
    if word is "":
        print(answer)
        return
    for i in range(len(word)):
        ch = word[i]
        left = word[0:i]
        right = word[i+1:]
        rest = left + right
        find_anagrams(rest,answer+ch)

find_anagrams("ABC","")
