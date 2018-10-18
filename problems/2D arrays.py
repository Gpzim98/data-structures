"""
https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&play
list_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
"""

def hourglassSum(arr):
    totais = []
    sum = 0

    for linha in range(0, 4):
        for coluna in range(0, 4):
            sum = arr[linha][coluna] + arr[linha][coluna + 1] + arr[linha][coluna + 2]
            sum += arr[linha + 1][coluna + 1]
            sum += arr[linha + 2][coluna] + arr[linha + 2][coluna + 1] + arr[linha + 2][coluna + 2]
            totais.append(sum)

    return max(totais)


arr =[
    [1, 1, 1, 0, 0, 0],
    [0, 1, 0, 0, 0, 0],
    [1, 1, 1, 0, 0, 0],
    [0, 0, 2, 4, 4, 0],
    [0, 0, 0, 2, 0, 0],
    [0, 0, 1, 2, 4, 0]
]
print(hourglassSum(arr))

