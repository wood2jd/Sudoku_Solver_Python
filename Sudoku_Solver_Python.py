import random
import numpy as np

#Sudoku Solve in Python
#Coding Practice

#SudokuGrid = [][]
ValidNumbers = [1,2,3,4,5,6,7,8,9]
ExampleStartGrid = np.array([[0,2,0,0,0,4,3,0,0],
							[9,0,0,0,2,0,0,0,8],
							[0,0,0,6,0,9,0,5,0],
							[0,0,0,0,0,0,0,0,1],
							[0,7,2,5,0,3,6,8,0],
							[6,0,0,0,0,0,0,0,0],
							[0,8,0,2,0,5,0,0,0],
							[1,0,0,0,9,0,0,0,3],
							[0,0,9,8,0,0,0,6,0],])

ExampleSolvedGrid =np.array([[8,2,7,1,5,4,3,9,6],
							[9,6,5,3,2,7,1,4,8],
							[3,4,1,6,8,9,7,5,2],
							[5,9,3,4,6,8,2,7,1],
							[4,7,2,5,1,3,6,8,9],
							[6,1,8,9,7,2,4,3,5],
							[7,8,6,2,3,5,9,1,4],
							[1,5,4,7,9,6,8,2,3],
							[2,3,9,8,4,1,5,6,7]])

ExampleErrorRowGrid =np.array([	[8,2,7,3,5,4,3,9,6],
								[9,6,5,1,2,7,1,4,8],
								[3,4,1,6,8,9,7,5,2],
								[5,9,3,4,6,8,2,7,1],
								[4,7,2,5,1,3,6,8,9],
								[6,1,8,9,7,2,4,3,5],
								[7,8,6,2,3,5,9,1,4],
								[1,5,4,7,9,6,8,2,3],
								[2,3,9,8,4,1,5,6,7]])

ExampleErrorColumnGrid =np.array([	[8,2,7,1,5,4,3,9,6],
									[9,6,5,3,2,7,1,4,8],
									[3,4,1,6,8,9,7,5,2],
									[5,9,3,4,6,8,2,7,1],
									[4,7,2,5,1,3,6,8,9],
									[6,1,8,9,7,2,4,3,5],
									[7,8,6,2,3,5,9,1,4],
									[1,5,4,7,9,6,8,2,3],
									[1,3,9,8,4,2,5,6,7]])

def CheckForGridCompletion(grid):
	#Function checks that all values in the grid are numbers 1-9 
	# & that the grid is the correct size
	if len(grid) != 9:
		return false
	rows = grid.shape[0]
	cols = grid.shape[1]
	for x in range(0, rows):
		for y in range(0,cols):
			if grid[x][y] not in ValidNumbers:
				return False
	return True

def CheckValidSolution(grid):
	#Verifies that the solution to the sudoku
	#This is my initial idea for how to solve
	#Method checks each square left to right, top to bottom to verify that all 
	#3 conditions are met
	if not CheckForGridCompletion(grid):
		return False
	#Check for any rows that have duplicate numbers
	for row in grid:
		elems = set()
		for elem in row:
			if elem in elems:
				return False
			else:
				elems.add(elem)	
	#Check for any columns with duplicate numbers
	for col in grid.T:
		elems = set()
		for elem in col:
			if elem in elems:
				return False
			else:
				elems.add(elem)

	#Else return true
	return True


def PrintGrid(grid):
	for row in grid:
		print(row)


#print(CheckForGridCompletion(ExampleStartGrid))
#print(CheckForGridCompletion(ExampleSolvedGrid))


#PrintGrid(SudokuGrid)
#PrintGrid(ExampleStartGrid)
#PrintGrid(ExampleSolvedGrid)

print(CheckValidSolution(ExampleSolvedGrid))
print(CheckValidSolution(ExampleErrorRowGrid))
print(CheckValidSolution(ExampleErrorColumnGrid))












































