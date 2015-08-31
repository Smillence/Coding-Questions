'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"
Write the code that will take a string and make this conversion given a number of rows:

string convert(string text, int nRows);
convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".
'''
class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1:
            return s
        
        n = 2*numRows-2
        result = ''
        l = len(s)
        
        # the first row
        for i in xrange(0, l, n):
            result += s[i]
        
        # rows in between
        for i in xrange(1,numRows-1):
            j = i
            while j < l+i-(n-i):
                result += s[j]
                result += s[j+(n-i)-i]
                j += n
            # if the number of chars in this row is odd
            if j < l:
                result += s[j]

        # the last row
        for i in xrange(numRows - 1, l, n):
            result += s[i]
            
        return result