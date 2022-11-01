class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        
       
        r=len(grid)
        c=len(grid[0])
        ans=[-1]*c
        
        def dfs(i,j,arr):
            
            if i+1>r:
                return j
            
            if arr[i][j]==1 and j+1<c and arr[i][j+1]==1:
                return dfs(i+1,j+1,arr)
            elif j-1>=0 and arr[i][j]==-1  and arr[i][j-1]==-1:
                return dfs(i+1,j-1,arr)
            elif arr[i][j]==1 and j+1>c:
                return -1
            else:
                return -1
            
        
        
        
        for i in range(c):
            ans[i]=dfs(0,i,grid)
        return ans
        
