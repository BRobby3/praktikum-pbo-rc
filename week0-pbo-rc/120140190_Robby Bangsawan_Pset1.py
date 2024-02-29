# Input number (n) from user
n = int(input("Enter a number: "))

# Loop for triangle 
for i in range(1, n + 1):
	# Print spaces between stars
	for j in range(n - i):
		print(" ", end="")

	# Print the stars
	for k in range(2 * i - 1):
		print("*", end="")

	# Move to new line
	print()
