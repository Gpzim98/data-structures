# check if the th bit position is set
# Shift the number 1 N position then applies &, 
# if it is not zero meanis that the th bit position is set

def is_th_bit_set(number, position):
	return bool(number & (1 << position))


print(is_th_bit_set(2 ,0))