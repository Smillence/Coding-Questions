class Solution(object):
    def isPalindrome(self, s):
        return s == s[::-1]
    def longestPalindromeBruthForce(self, s):
        n = len(s)
        for max in xrange(n,-1,-1):
            for j in xrange(n-max+1):
                if self.isPalindrome(s[j:j+max]):
                    return s[j:j+max]
    def longestPalindromeDP(self, s):
        n = len(s)
        if n <= 2:
            return s
            
        str = ''
        
        table = [[False for _ in range(n+1)] for _ in range(n)]
        
        # substring with length 1
        for j in xrange(n):
            table[j][j+1] = True
            str = s[j:j+1]
        
        # check for substring with length 2
        for j in xrange(n-1):
            table[j][j+2] = self.isPalindrome(s[j:j+2])
            if table[j][j+2]:
                str = s[j:j+2]
        
        # check for substring with length > 2
        for i in xrange(2,n):
            for j in xrange(n-i):
                if s[j] == s[j+i] and table[j+1][j+i]:
                    table[j][j+i+1] = True
                    str = s[j:j+i+1]
                else:
                    table[j][j+i+1] = False
        return str    
    def longestPalindrome_1228ms(self, s):
        n = len(s)
        if n <= 1:
            return s
            
        max_length = 0
        start = 0
        for i in xrange(n):
            # odd length
            left = right = i
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if max_length < right - left - 1:
                max_length = right - left - 1
                start = left + 1
            
            # even length
            left, right = i, i+1
            while left >=0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            if max_length < right - left - 1:
                max_length = right - left - 1
                start = left + 1
        return s[start:start+max_length] 
    def longestPalindrome_648ms(self, s):
        n = len(s)
        if n <= 1:
            return s
            
        max_length = start =0
        
        i = 0
        while i < n - max_length/2:
            # odd length
            if s[i-max_length/2+1] == s[i+max_length/2-1]:
                left = right = i
                while left >=0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                if max_length < right - left - 1:
                    max_length = right - left - 1
                    start = left + 1
            # even length
            if s[i-max_length/2+1] == s[i+max_length/2]:
                left, right = i, i+1
                while left >=0 and right < n and s[left] == s[right]:
                    left -= 1
                    right += 1
                if max_length < right - left - 1:
                    max_length = right - left - 1
                    start = left + 1
            i += 1
            
        return s[start:start+max_length]