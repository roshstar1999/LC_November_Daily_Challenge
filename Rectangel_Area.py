class Solution:
    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        
        totalArea=abs((ax1-ax2)*(ay1-ay2))+abs((bx1-bx2)*(by1-by2))
        
		#checking if the two rectangeles are intersecting or not
		#just check if the x or y cordinate of top right corner of each rectangle is smaller than or equal to  the bottom  left corner  of the other rectangle
		#if yes , then that means they are not intersecting, just return the toal of individual rectangles
			
        if bx1>=ax2 or bx2<=ax1 or by2<ay1 or ay2<by1:
            return totalArea
        
        #else, return the total area- the intersecting area 
		
        return totalArea-abs((max(ax1,bx1)-min(ax2,bx2))*(max(ay1,by1)-min(ay2,by2)))
		
		# feel free to reach out if any doubts
