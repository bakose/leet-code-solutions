class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        list = ["" for _ in range(numRows)]    
        idx = 0
        offset = -1
        for i in range(len(s)):        
            list[idx] += s[i]
            if idx % (numRows - 1) == 0:
                offset *= -1

            idx += offset
        return ''.join(list)