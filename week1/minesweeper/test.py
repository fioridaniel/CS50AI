from minesweeper import *

# initializing constants
HEIGHT=8 
WIDHT=8
MINES=8

# ate agora parece que esta funcionando bem
def adjacentCells(cell):
    """ returns the set of adjacent cells (i, j) for cell """    
    adj_cells = set()
    i, j = cell
    
    for row in range(8):
        for col in range(8):
    
            adj_cell = row, col
            delta_row = abs(i - row)
            delta_col = abs(j - col)
            
            # mesma linha
            if delta_row == 0 and delta_col == 1:
                adj_cells.add(adj_cell)
            
            # mesma coluna
            elif delta_row == 1 and delta_col == 0:
                adj_cells.add(adj_cell)
            
            # diagonal
            elif delta_row == 1 and delta_col == 1:
                adj_cells.add(adj_cell)
    
    return adj_cells


# More generally, any time we have two sentences set1 = count1 and set2 = count2 
# where set1 is a subset of set2, then we can construct the new sentence set2 - set1 = count2 - count1
# Consider the example above to ensure you understand why that’s true.

def main():
    print("starting tests ...")
    adj_cells = adjacentCells((3, 3))     
    print(adj_cells)

main()
