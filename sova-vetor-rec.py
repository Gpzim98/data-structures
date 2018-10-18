a = [1,2,3,4,5,6]

def soma(vetor, size):

	if size == 1:
		return a[0]
	else:
		return vetor[size - 1] + soma(vetor, size - 1)

print(soma(a, 6))