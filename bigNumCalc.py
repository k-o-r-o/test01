from bigNum import bigNum

def read_operations(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        operations = []
        for line in lines:
            operations.append(line.strip())
    return operations

def perform_operation(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        try:
            return num1.__div__(num2)  # Use the __div__ method of bigNum for division
        except ZeroDivisionError:
            print("Cannot divide by zero")
            return None
    else:
        print("Invalid operator")
        return None

def calculate_big_nums(filename):
    operations = read_operations(filename)
    result = bigNum(operations[0])
    print("******************\nBigNum Calculator\n******************")
    for i in range(1, len(operations), 2):
        operator = operations[i]
        next_num = bigNum(operations[i+1])
        print(f"{str(result)} {operator} {str(next_num)} = ", end="")
        result = perform_operation(result, operator, next_num)
        print(str(result))
    print("******************\nFinal result\n******************")
    print(str(result))

calculate_big_nums("bigNums.txt")