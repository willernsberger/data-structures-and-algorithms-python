# given a number, count the number of 1-bits

# linear time with respect to the number of bits in the given number
# constant space for the variable(s)
def count_bits(num):
    count = 0
    while num > 0:
        if num%2 == 1:
            count +=1
        num = num >> 1
    return count

print(count_bits(121))
