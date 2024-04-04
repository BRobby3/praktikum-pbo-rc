import random

matrix = [[{'?': 'safe'} for _ in range(3)] for _ in range(3)]

# Change one of the 9 elements to 'bomb'
row, col = random.randint(0, 2), random.randint(0, 2)
matrix[row][col]['?'] = 'bomb'

# Safe Box Tracker
safe_boxes = 8

# Opened Box Tracker
opened_boxes = set()

# Print Matrix
for row in matrix:
	print(' '.join([key for cell in row for key in cell.keys()]))

while True:
		print("Select a box by row and column (0-2):")
		while True:
				user_row = int(input("Enter row: "))
				if 0 <= user_row < 3:
						break
				print("Invalid input! Please enter a number between 0 and 2.")

		while True:
				user_col = int(input("Enter column: "))
				if 0 <= user_col < 3:
						break
				print("Invalid input! Please enter a number between 0 and 2.")

		# Create unique identifier for the box
		box_id = (user_row, user_col)

		# Check if the box has been opened
		if box_id in opened_boxes:
				print("You have already opened this box!")
				continue

		# Add the opened box to the set
		opened_boxes.add(box_id)

		selected_box = matrix[user_row][user_col]
		if selected_box['?'] == 'bomb':
				# Game over
				selected_box['X'] = selected_box.pop('?')
				for row in matrix:
					print(' '.join([key for cell in row for key in cell.keys()]))
				print("Game Over!")
				break
		else:
				# Reveal the safe box and decrement the number of safe boxes
				selected_box['O'] = selected_box.pop('?')
				safe_boxes -= 1

				for row in matrix:
						print(' '.join([key for cell in row for key in cell.keys()]))

				# Check if the user has won
				if safe_boxes == 0:
						print("You Win!")
						break
