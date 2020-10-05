# given a roman numeral, convert it to a decimal number


# O(n) time for the single pass
# O(1) space for the dictionary
def numeral_to_decimal(numeral):
    m = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    decimal = 0
    for index in range(-1, -len(numeral) - 1, -1):
        # I... if the element is at the end of the numeral, just add it to decimal
        if index == -1:
            decimal += m[numeral[index]]
        # II if the element precedes the same element, just add it to decimal
        # VI if the element is greater than the previous element, just add it to decimal
        elif m[numeral[index]] >= m[numeral[index + 1]]:
            decimal += m[numeral[index]]
        # IV if the element is less than the previous element, subtract it from the decimal
        elif m[numeral[index]] < m[numeral[index - 1]]:
            decimal -= m[numeral[index]]
    return decimal


# test string
numeral = 'MCMXIII'  # 1913

# driver
print(numeral_to_decimal(numeral))
