def DecimalToBinary(n):
    return("{0:b}".format(int(n)))

d = DecimalToBinary(9)
print(d)

binary_number = "1001"  # Replace this with your binary number
decimal_representation = int(binary_number, 2)

print(f"The decimal representation of {binary_number} is {decimal_representation}")


def bin_dec(num):
       return int(num,2)