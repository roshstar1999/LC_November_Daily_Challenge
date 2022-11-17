class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        totalArea=abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))
        
        if bx1>=ax2 or bx2<=ax1 or by2<ay1 or ay2<by1:
            return totalArea
        
        
        return totalArea-abs((max(ax1,bx1)-min(ax2,bx2))*(max(ay1,by1)-min(ay2,by2)))
        
      
        
        
        
        
