import pygame 
import random 

pygame.init()

pygame.display.set_caption('2048')

LENGTH = 600
WINDOW = pygame.display.set_mode((LENGTH, LENGTH))

BACKGROUND = [112, 97, 85]
CELL = [163, 144, 129]

COLOR_DICT = {
	"2" : [238, 228, 218],
	"4" : [237, 224, 200],
	"8" : [242, 177, 121],
	"16" : [245, 149, 99],
	"32" : [246, 124, 95],
	"64" : [246, 94, 59],
	"128" : [237, 207, 114],
	"256" : [237, 204, 97],
	"512" : [237, 200, 8],
	"1024" : [237, 197, 63],
	"2048" : [237, 194, 46]
}

#spawns a number in a random empty cell 
def spawn_cell(grid):
	empty = []
	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 0:
				empty.append([row, col])
	
	rand_cell = random.choice(empty)
	rand_num = random.random()

	#90% chance that the new number is 2 and 10% chance that it is a 4
	if rand_num > 0.1:
		grid[rand_cell[0]][rand_cell[1]] = 2
	else: 
		grid[rand_cell[0]][rand_cell[1]] = 4

#function that moves all the number cells to the input direction 
def move(grid, direction):
	#create a copy of the grid to compare differences after changes are made to the original 
	copy = copy_grid(grid)

	new_pos = []
	if direction == "up":
		new_pos = [-1, 0]
	elif direction == "down":
		new_pos = [1, 0]
	elif direction == "right":
		new_pos = [0, 1]
	elif direction == "left":
		new_pos = [0, -1] 

	#if moving down or right, iterate through the grid backwards 
	if direction == "down" or direction == "right":
		for row in range(len(grid) - 1, -1, -1):
			for col in range(len(grid[0]) - 1, -1, -1):
				#check if the current space is not empty 
				if grid[row][col] != 0:
					num = grid[row][col]
					if direction == "right": 
						#iterate from that position to the end of the row 
						for i in range(col, len(grid[0])):  
							if check_new_pos(grid, [row, i], new_pos):
								#if the next position is empty, move the current value to that
								#position and change the current position to 0 
								if grid[row + new_pos[0]][i + new_pos[1]] == 0:
									grid[row + new_pos[0]][i + new_pos[1]] = grid[row][i]
									grid[row][i] = 0
								#if the next position is not empty combine them 
								elif grid[row + new_pos[0]][i + new_pos[1]] == num:
									grid[row + new_pos[0]][i + new_pos[1]] = 2 * num  
									grid[row][i] = 0
								else:
									break
					else:
						#iterate from that position to the end of the column 
						for i in range(row, len(grid)):  
							if check_new_pos(grid, [i, col], new_pos):
								#if the next position is empty, move the current value to that
								#position and change the current position to 0 
								if grid[i + new_pos[0]][col + new_pos[1]] == 0:
									grid[i + new_pos[0]][col + new_pos[1]] = grid[i][col]
									grid[i][col] = 0
								#if the next position is not empty combine them 
								elif grid[i + new_pos[0]][col + new_pos[1]] == num:
									grid[i + new_pos[0]][col + new_pos[1]] = 2 * num  
									grid[i][col] = 0
								else:
									break
	#if moving up or left iterate through the grid normally 
	else: 
		for row in range(len(grid)):
			for col in range(len(grid[0])):
				#check if the current space is not empty
				if grid[row][col] != 0:
					num = grid[row][col]
					if direction == "left":
					#iterate backwards from that position to the end of the row 
						for i in range(col, -1, -1):
							if check_new_pos(grid, [row, i], new_pos):
								#if the next position is empty, move the current value to that
								#position and change the current position to 0 
								if grid[row + new_pos[0]][i + new_pos[1]] == 0:
									grid[row + new_pos[0]][i + new_pos[1]] = grid[row][i]
									grid[row][i] = 0
								#if the next position is not empty combine them 
								elif grid[row + new_pos[0]][i + new_pos[1]] == num:
									grid[row + new_pos[0]][i + new_pos[1]] = 2 * num  
									grid[row][i] = 0
								else:
									break
					else:
						#iterate from that position to the end of the column
						for i in range(row, -1, -1): 
							if check_new_pos(grid, [i, col], new_pos):
								#if the next position is empty, move the current value to that
								#position and change the current position to 0 
								if grid[i + new_pos[0]][col + new_pos[1]] == 0:
									grid[i + new_pos[0]][col + new_pos[1]] = grid[i][col]
									grid[i][col] = 0	
								#if the next position is not empty combine them 
								elif grid[i + new_pos[0]][col + new_pos[1]] == num:
									grid[i + new_pos[0]][col + new_pos[1]] = 2 * num  
									grid[i][col] = 0
								else:
									break 

	if copy != grid:
		spawn_cell(grid)	

#checks that the given position is valid and there is not an indexing error
def check_new_pos(grid, curr_pos, new_pos):
	row_pos = curr_pos[0] + new_pos[0]
	col_pos = curr_pos[1] + new_pos[1]

	if row_pos >= 0 and row_pos < len(grid) and col_pos >= 0 and col_pos < len(grid[0]):
		return True
	else: 
		return False

#makes a copy of the input array 
def copy_grid(grid):
	copy = [[0 for col in range (4)] for row in range(4)]

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			copy[row][col] = grid[row][col]

	return copy

#fix: update to check if player can still combine
#checks the grid is full so no new numbers are added
def check_full(grid):
	moves = ["up", "down", "right", "left"]
	for i in range(len(moves)):
		copy = copy_grid(grid)
		move(copy, moves[i])
		if grid != copy:
			return False

	return True

#returns total count and max value in grid
def get_count(grid):
	total = 0
	max_value = 0 

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] != 0:
				total += 1
			if grid[row][col] > max_value:
				max_value = grid[row][col]

	return total, max_value

def AI(grid, depth):                          
	possible_moves = ["up", "down", "left", "right"]
	best_move = None
	highest_score = 0

	if depth == 0:
		return evaluate_grid(grid), best_move

	for i in range(len(possible_moves)):
		copy = copy_grid(grid)
		move(copy, possible_moves[i])
		score = AI(copy, depth - 1)[0]

		if score > highest_score:
			highest_score = score
			best_move = possible_moves[i]

	return highest_score, best_move

#gives a score to the current grid to evalute how good it is
def evaluate_grid(grid):
	score = 0
	grid_bias = [[10, 4, 2, 1],
				 [4, 2, -1, -2],
				 [2, -1, -1, -2],
				 [1, -2, -2, -2]]

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			score += grid[row][col] * grid_bias[row][col]

			if check_new_pos(grid, [row, col], [row + 1, col + 1]):
				if grid[row][col] == grid[row + 1][col] or grid[row][col] == grid[row][col + 1]:
					score += 4 * grid[row][col]
				elif grid[row][col] / 2  == grid[row + 1][col] or grid[row][col] / 2 == grid[row][col + 1]:
					score += 3 * grid[row][col]
				elif grid[row][col] == grid[row + 1][col] / 2 or grid[row][col] == grid[row][col + 1] / 2:
					score += 3 * grid[row][col]

	if check_full(grid):
		score -= 1000

	return score

#manages the graphics 
def update_display(win, grid):
	win.fill(BACKGROUND)

	font = pygame.font.Font('freesansbold.ttf', 45)

	cell_size = 130
	grid_length = (LENGTH - (cell_size * len(grid))) / (len(grid) + 1)
	start_row = grid_length
	start_col = grid_length 

	for row in range(len(grid)):
		for col in range(len(grid[0])):
			if grid[row][col] == 0:
				pygame.draw.rect(win, CELL, (start_col, start_row, cell_size, cell_size), border_radius=10)
			else: 
				num = grid[row][col]
				color = COLOR_DICT.get(str(num))
				pygame.draw.rect(win, color, (start_col, start_row, cell_size, cell_size), border_radius=10)
				num_text = font.render(str(num), True, (112, 102, 95))
				text_rect = num_text.get_rect()
				text_rect.center = (start_col + (cell_size // 2), start_row + (cell_size // 2))
				win.blit(num_text, text_rect)
			start_col += cell_size + grid_length
		start_col = grid_length
		start_row += cell_size + grid_length

	pygame.display.update()

def main():
	grid = [[0 for col in range (4)] for row in range(4)]
	spawn_cell(grid)
	spawn_cell(grid)

	isAI = False 

	while True:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
				quit()

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_UP:
					move(grid, "up")
				if event.key == pygame.K_DOWN:
					move(grid, "down")
				if event.key == pygame.K_RIGHT:
					move(grid, "right")
				if event.key == pygame.K_LEFT:
					move(grid, "left")	

				if event.key == pygame.K_SPACE: 
					isAI = not isAI 

		if isAI:
			if get_count(grid)[1] < 512:
				move(grid, AI(grid, 5)[1])
			elif get_count(grid)[1] < 1024: 
				if get_count(grid)[0] <= 12:
					move(grid, AI(grid, 5)[1])
				else:
					move(grid, AI(grid, 6)[1])
			else:
				if get_count(grid)[0] <= 14:
					move(grid, AI(grid, 6)[1])
				else:
					move(grid, AI(grid, 7)[1])

		if get_count(grid)[1] == 2048:
			isAI = False

		if check_full(grid):
			main()

		update_display(WINDOW, grid)

if __name__ == '__main__':
	main()
