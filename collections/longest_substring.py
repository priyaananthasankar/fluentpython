
def lengthOfLongestSubstring(s):
    
        # String s="";
        # int res=-1;
        # if(so.isEmpty())
        #     return 0;
        # for(char c:so.toCharArray())
        # {
        #     String str=String.valueOf(c);
        #     if(s.contains(str))
        #     {
        #         s=s.substring(s.indexOf(c)+1);
                
        #     }
        #     s=s+str;
        #     res=Math.max(res,s.length());
        # }
        # return res;
        final_str = ""
        res = -1
        if s == "":
            return 0
        for i in range(len(s)):
            if s[i] not in final_str:
                final_str = final_str + s[i]
            else:
                idx = final_str.index(s[i])
                final_str = final_str[idx+1:] + s[i]
            res = max(res,len(final_str))
        return res
                

lengthOfLongestSubstring("abcabcbb")
