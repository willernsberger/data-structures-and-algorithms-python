# given a decimal number, determin the number of consecute bit ones
# in the binary representation of the decimal number


# O(n) time with respect to the number of binary digits
# O(1) space
def consecutive_bit_ones_string_manipulation(decimal):
    consecutive, count = 0, 0
    binary_string = str(bin(decimal))
    index = len(binary_string) - 1
    while binary_string[index] == '1' or binary_string[index] == '0':
        # if it is a zero, evaluate count against max and reset count
        if binary_string[index] == '0':
            consecutive = max(count, consecutive)
            count = 0
        # if it is a one, increment count
        if binary_string[index] == '1':
            count += 1
        index -= 1
    consecutive = max(count, consecutive)
    return consecutive


# O(n) time with respect to the number of binary digits
# O(1) space
def consecutive_bit_ones_modulo(decimal):
    consecutive, count = 0, 0

    while decimal > 0:
        remainder = decimal%2
        if remainder == 0:
            consecutive = max(count, consecutive)
            count = 0
        if remainder == 1:
            count += 1
        decimal //= 2
    return consecutive


# O(n) time with respect to the number of binary digits
# O(1) space
def consecutive_bit_ones_bit_shifing(decimal):
    consecutive, count = 0, 0
    bit_mask = 1

    while decimal > 0:
        remainder = decimal & bit_mask
        if remainder == 0:
            consecutive = max(count, consecutive)
            count = 0
        if remainder == 1:
            count += 1
        decimal = decimal >> 1
    return consecutive


# testing data
decimal_number = 12345  # 11000000111001

# driver
print(consecutive_bit_ones_bit_shifing(decimal_number))
