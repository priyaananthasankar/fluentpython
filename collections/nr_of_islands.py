def nr_of_islands(grid):
    columns = len(grid[0])
    rows = len(grid)
    islands = 0
    for i in range(rows):
        for j in range(columns):
            if grid[i][j] == "1":
                # start island count
                islands = islands + 1
                visit(i,j,grid,rows,columns)
    return islands

def visit(i,j,grid,r,c):
    
    # check out of bounds
    if i < 0 or j < 0 or i >= r or j >= c:
        return
    if grid[i][j] == "0" or grid[i][j] == "2":
        return
    else:
        grid[i][j] = "2" # mark visited as 2
        
        # visit the adjacent neighbor on 4 sides
        visit(i+1,j,grid,r,c)
        visit(i-1,j,grid,r,c)
        visit(i,j+1,grid,r,c)
        visit(i,j-1,grid,r,c)
        
    

print(nr_of_islands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],
["0","0","0","0","0"]]))
print(nr_of_islands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))