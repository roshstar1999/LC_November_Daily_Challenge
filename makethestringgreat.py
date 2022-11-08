class Solution:
    def makeGood(self, s: str) -> str:
        
        
        res=[]
        
        for i in s:
            
            if res and abs(ord(res[-1])-ord(i))==32:
                res.pop()
            
            else:
                res.append(i)
        return ''.join(res)
        
        
                
       
            
        
        
