# 20th Excise: Exponent Function
# YouTube Vid: Learn Python - Full Course for Beginners
# URL: https://youtu.be/rfscVS0vtbw


# Create a function with two parms, the base number and the power on which to times it by
def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result


print(raise_to_power(3, 4))