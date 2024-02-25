from operations import binary_operations as operate


while True:
    print("Menu-2 (Binary Operations)")
    print("[1] Division")
    print("[2] Multiplication")
    print("[3] Subtraction")
    print("[4] Addition")
    print("[5] Negative (2's Complement)")
    print("[6] Quit") 
    choice = input("Enter your choice (1-6): ")

    if choice in ['1', '2', '3', '4', '5']:
        if choice != '5':
            operation = input("[1] Signed\n[2] Unsigned\nEnter the operation type: ")
            if operation.upper() == '1':
                binary1 = input("Enter the first binary number: ")
                decimal1 = operate.signed_binary_to_decimal(binary1)
            elif operation.upper() == '2':
                binary1 = input("Enter the first binary number: ")
                decimal1 = operate.unsigned_binary_to_decimal(binary1)
            else:
                print("Invalid operation type. Please enter '1' for signed or '2' for unsigned.")
                continue
        else:
            binary = input("Enter the binary number: ")
            result = operate.twos_complement(binary)
            print("Two's complement result:", result)
            continue

        binary2 = input("Enter the second binary number: ")
        decimal2 = operate.signed_binary_to_decimal(binary2) if operation.upper() == '1' else operate.unsigned_binary_to_decimal(binary2)
        
        if choice == '1':
            if decimal2 != 0:
                result = operate.divide_decimals(decimal1, decimal2)
            else:
                print("Cannot divide by zero!")
                continue
        if choice == '2':
            result = operate.multiply_decimals(decimal1, decimal2)
        elif choice == '3':
            result = operate.subtract_decimals(decimal1, decimal2)
        elif choice == '4':
            result = operate.add_decimals(decimal1, decimal2)


        
        if operation.upper() == '1':
            print("Result (signed) in binary:", operate.signed_decimal_to_binary(result))
        elif operation.upper() == '2':
            print("Result (unsigned) in binary:", operate.unsigned_decimal_to_binary(result))

        input('Press Enter to continue...')
    elif choice == '6':
        print("Exiting the program. Goodbye!")
        break
    else:
        print("Invalid choice")
