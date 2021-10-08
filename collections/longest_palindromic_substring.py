def longestPalindrome(s):
    n = len(s)
    # initialize the memoization array
    dp = [[False for i in range(n)] for j in range(n)]
    length = 0
    lastIndex = 0
    for g in range(n):
        i = 0
        j = g
        while j < n:
            dp[i][j] = (i==j) or (g == 1 and s[i] == s[j])or (s[i] == s[j] and dp[i+1][j-1])
            if dp[i][j] == True:
                length = g+1
                lastIndex = j+1
            i = i+1
            j = j+1
    return s[abs(length-lastIndex):lastIndex]

print(longestPalindrome("a"))
