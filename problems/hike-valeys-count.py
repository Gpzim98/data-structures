def countingValleys(n, s):
    current = valleys = 0

    for i in range(0, len(s)):
        current = current + 1 if s[i] == 'U' else current - 1

        if current == 0 and s[i] == 'U':
            valleys += 1

    return valleys

print(countingValleys(10, 'DDUDDUUDUU')) # 1
print(countingValleys(8, 'UDDDUDUU')) # 1
print(countingValleys(8, 'DDUUDDUDUUUD')) # 2
print(countingValleys(10, 'UDUUUDUDDD')) # 0
