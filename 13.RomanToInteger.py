class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        convert={'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1} 
        Sum=0
        i=0
        for i in range(0,len(s)-1):
            if (convert[s[i]]>=convert[s[i+1]]):
                Sum=Sum+convert[s[i]]
            else:
                Sum=Sum-convert[s[i]]
        Sum += convert[s[len(s)-1]]
        return Sum 