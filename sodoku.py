def find_next_cell_to_fill(grid, i, j):
        for x in range(i, 9):
                for y in range(j, 9):
                        if grid[x][y] == 0:
                                return x, y
        for x in range(0, 9):
                for y in range(0, 9):
                        if grid[x][y] == 0:
                                return x, y
        return -1, -1

def is_valid(grid, i, j, e):
        row_okay = all([e != grid[i][x] for x in range(9)])
        if row_okay:
                column_okay = all([e != grid[x][j] for x in range(9)])
                if column_okay:
                        # Finding the top left x,y co-ordinates of the section containing the i,j cell
                        sec_top_x, sec_top_y = 3 * (i // 3), 3 * (j // 3) # Floored quotient should be used here
                        for x in range(sec_top_x, sec_top_x + 3):
                                for y in range(sec_top_y, sec_top_y + 3):
                                        if grid[x][y] == e:
                                                return False
                        return True
        return False

def solve_sudoku(grid, i = 0, j = 0):
        i,j = find_next_cell_to_fill(grid, i, j)
        if i == -1:
                return True
        for e in range(1, 10):
                if is_valid(grid, i, j, e):
                        grid[i][j] = e
                        if solve_sudoku(grid, i, j):
                                return True

                        # Undo the current cell for backtracking
                        grid[i][j] = 0
        return False

def print_board(m):
	# If no board to print, print No Solution
	if m is None:
		print("No Solution")
		return
	line = "-" * 25
	if m == []:
		print("Empty Matrix")
	num_of_rows = len(m)
	num_of_cols = len(m[0])

	for i in range(num_of_rows):
		# print line every 3 rows
		if i % 3 == 0:
			print(line)
		row_to_print = ""
		for j in range(num_of_cols):
			# print vertical bar every 3 column
			if j % 3 == 0:
				row_to_print += "| "
			value = str(m[i][j] if m[i][j] > 0 else " ")
			row_to_print += value + " "
		row_to_print += "|"
		print(row_to_print)
	print(line)

board = [[8,0,0,0,0,0,0,0,0],
		[0,0,3,6,0,0,0,0,0],
		[0,7,0,0,9,0,2,0,0],
		[0,5,0,0,0,7,0,0,0],
		[0,0,0,0,4,5,7,0,0],
		[0,0,0,1,0,0,0,3,0],
		[0,0,1,0,0,0,0,6,8],
		[0,0,8,5,0,0,0,1,0],
		[0,9,0,0,0,0,4,0,0]]

print("With Sodoku: ")
print_board(board)

print("Solving ...")
solve_sudoku(board)

print("Solution:")
print_board(board)