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

    whole_binary = bin(whole_part)[2:]

    fraction_binary = ''
    while fraction_part > 0:
        fraction_part *= 2
        if fraction_part >= 1:
            fraction_binary += '1'
            fraction_part -= 1
        else:
            fraction_binary += '0'

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


print(signed_decimal_to_binary(52))
print(signed_binary_to_decimal('1000.01'))
