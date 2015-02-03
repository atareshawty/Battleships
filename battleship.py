import random

print("Welcome to Battleship!!")
print("Below is your 10x10 war zone")

#create playing field and print it
field = []
for i in range(10):
	field.append(['O','O','O','O','O','O','O','O','O','O'])

def print_field(field):
	print ""
	for line in field:
		print " ".join(line)

print_field(field)

#Create ship spot
row = random.randint(0,8)
col = random.randint(0,9)
ship_position = [[row,col],[row + 1,col]]



#mark_spot places either 'X' for miss, or '!' for a hit in the board
def mark_spot(check,spot,field):
	if check:
		field[spot[0]][spot[1]] = "!"
	else:
		field[spot[0]][spot[1]] = "X"

def is_hit(guess_spot,ship_position):
	if guess_spot[0] == ship_position[0][0] or guess_spot[0] == ship_position[1][0] and guess_spot[1] == ship_position[0][1]:
		return True
	else:
		return False

hit_count = 0
miss_count = 0

while hit_count < 2 and miss_count < 15:
	row_guess = int(raw_input("Guess the row position: ")) - 1
	col_guess = int(raw_input("Guess the column position: ")) - 1
	guess_spot = [row_guess, col_guess]
	hit = is_hit(guess_spot,ship_position)

	if hit:
		print "Darn! You hit my battleship"
		hit_count += 1
	else:
		print "Haha! You missed :P"
		miss_count += 1

	mark_spot(hit, guess_spot, field)
	print_field(field)

if hit_count == 2:
	print "CONGRATS!! YOU SUNK MY BATTLESHIP"