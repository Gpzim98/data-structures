# Unset th bit

# 1 0 1 = 5
# 1 0 0 = 1 << 2)
# 0 0 1 = apply XOR
def unset_th_bit(number, position):
	return number ^ (1 << position)

# This case is using tilda to do 2's compliment 
# to move a zero to the specific position
#  1 0 1 = 5
#  0 0 1 = ~(1 << 2)
#  0 0 1 = apply & 
def unset_th_bit1(number, position):
	return number & ~(1 << position)

print(unset_th_bit(4, 1))
print(unset_th_bit1(4, 1))
