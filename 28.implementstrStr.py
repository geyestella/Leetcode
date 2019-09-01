class Solution(object):
    def strStr(haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if (needle==''):
            return 0 
        else:
            for i in range(len(haystack)-len(needle)+1):
                for j in range(len(needle)):
                    if (haystack[i+j]!=needle[j]):
                        break
                    if (j == len(needle)-1):
                        return i
            return -1
                    
                        
    print(strStr("aaaaa","a"))