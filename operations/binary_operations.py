
# class Test:
#     def __init__(self) -> None:
#         pass

#     def __str__(self) -> str:
#         return("Class Connected")


# def test_connect():
#     cls = Test()
#     return cls

# print(test_connect())

# hex_char = {
#     10: 'A',
#     11: 'B',
#     12: 'C',
#     13: 'D',
#     14: 'E',
#     15: 'F'
# }

# for i in hex_char:
#     print(i)

# dec = 5.6
# num = dec//1
# print(int(dec))

# print(5.6-5)

# print(float((str(dec))[1:]))

# bit = str(dec)
# print(bit.index('.'))

# def twos_complement(bit):
#     string = bit[::-1]
#     idx = 0
#     for i in string:
#         if i == '1':
#             idx = string.index(i)
#             break

#     bits = [for i in string ]

# string = '1001'
# new_string = []
# for i in range(len(string)):
#     if i == 0:
#         new_string.append(string[i])
#     else:
#         new_string.append('0')

# print(new_string)

# x = float(input("Enter: "))
# print(x)

def unsigned_binary_to_decimal(binary):
    whole, _, fractional = binary.partition('.')
    decimal = int(whole, 2)
    if fractional:
        fraction_decimal = sum(int(bit) * (2 ** -(i + 1))
                               for i, bit in enumerate(fractional))
        decimal += fraction_decimal
    return decimal


def unsigned_decimal_to_binary(decimal):
    whole_part = int(decimal)
    fraction_part = decimal - whole_part if decimal != whole_part else 0.0

    whole_binary = bin(whole_part)[2:]

    fraction_binary = ''
    while fraction_part > 0:
        fraction_part *= 2
        if fraction_part >= 1:
            fraction_binary += '1'
            fraction_part -= 1
        else:
            fraction_binary += '0'

    return whole_binary + ('.' + fraction_binary if fraction_binary else '')


def signed_binary_to_decimal(binary):
    sign_bit = int(binary[0])
    number_parts = binary[1:].split('.')

    whole_part = int(number_parts[0], 2)
    fraction_part = 0

    if len(number_parts) > 1:
        fraction_part = sum(int(bit) * (2 ** -(i + 1))
                            for i, bit in enumerate(number_parts[1]))

    decimal = whole_part + fraction_part

    if sign_bit == 1:
        # Convert the decimal to its negative equivalent
        if '.' in binary:
            decimal = -(sign_bit * 2 **
                        ((len(binary[0: binary.index('.')]) - 1))) + decimal
        else:
            decimal = -(sign_bit * 2 ** ((len(binary) - 1))) + decimal

    return decimal


def signed_decimal_to_binary(decimal):
    if decimal == 0:
        return '0'

    sign_bit = '1' if decimal < 0 else '0'
    abs_decimal = abs(decimal)
    whole_part = int(abs_decimal)
    fraction_part = abs_decimal - whole_part if abs_decimal != whole_part else 0.0
    # print(whole_part)

    whole_binary = bin(whole_part)[2:]
    # print(whole_binary)

    fraction_binary = ''
    while fraction_part > 0:
        fraction_part *= 2
        if fraction_part >= 1:
            fraction_binary += '1'
            fraction_part -= 1
        else:
            fraction_binary += '0'

    # Modified this part to handle both positive and negative - uzzi
    if decimal < 0:
        binary = sign_bit + \
            twos_complement(
                whole_binary + ('.' + fraction_binary if fraction_binary else ''))
    else:
        binary = sign_bit + whole_binary + \
            ('.' + fraction_binary if fraction_binary else '')

    return binary


def divide_decimals(decimal1, decimal2):
    return decimal1 / decimal2


def multiply_decimals(decimal1, decimal2):
    return decimal1 * decimal2


def subtract_decimals(decimal1, decimal2):
    return decimal1 - decimal2


def add_decimals(decimal1, decimal2):
    return decimal1 + decimal2


def twos_complement(binary):
    complement = ''.join('1' if bit == '0' else bit if bit ==
                         '.' else '0' for bit in binary)

    result = ''
    carry = 1
    for bit in complement[::-1]:
        if bit == '0' and carry == 1:
            result = '1' + result
            carry = 0
        elif bit == '1' and carry == 1:
            result = '0' + result
        else:
            result = bit + result

    return result

# Your other functions remain unchanged...


print(signed_decimal_to_binary(52))
print(signed_binary_to_decimal('1000.01'))
