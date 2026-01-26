def convertToDecimal(n: str) -> int:
    decimal_number = 0
    power = 0
    index = len(n) - 1
    while index >= 0:
        num = int(n[index]) * (2 ** power)
        decimal_number += num
        index -= 1
        power += 1
    return decimal_number
print(convertToDecimal("1101"))