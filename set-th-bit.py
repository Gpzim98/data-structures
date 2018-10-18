# Set the th bit of a number

def set_th_bit(number, position):
	coringa = 1 << position
	return number | coringa

print(set_th_bit(1, 0))