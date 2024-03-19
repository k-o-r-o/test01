from dblyLnkdLst import DoublyLinkedList


class bigNum:
    def __init__(self, value='0'):
        self.digits = DoublyLinkedList()
        self.sign = '+'
        if value[0] == '-':
            self.sign = '-'
            value = value[1:]
        for digit in reversed(value):
            self.digits.addLast(int(digit))

    def __add__(self, other):
        if not isinstance(other, bigNum):
            raise Exception("Operand must be bigNum")
        result = bigNum()
        remainder = 0
        digit_self = self.digits.head
        digit_other = other.digits.head
        while digit_self or digit_other or remainder:
            sum_val = remainder
            if digit_self:
                sum_val += digit_self.data
                digit_self = digit_self.next
            if digit_other:
                sum_val += digit_other.data
                digit_other = digit_other.next
            result.digits.addLast(sum_val % 10)
            remainder = sum_val // 10

        # Handle result sign based on the initial signs of the operands
        if self.sign == '-' and other.sign == '-':
            result.sign = '-'
        else:
            result.sign = '+'

        # Remove leading zeros from the result
        while len(result) > 1 and result.digits.head.data == 0:
            result.digits.removeFirst()

        return result
    
    def __sub__(self, other):
        if not isinstance(other, bigNum):
            raise Exception("Operand must be a bigNum")
        result = bigNum()
        borrow = 0
        digit_self = self.digits.head
        digit_other = other.digits.head
        while digit_self or digit_other:
            diff = borrow
            if digit_self:
                diff += digit_self.data
                digit_self = digit_self.next
            if digit_other:
                diff -= digit_other.data
                digit_other = digit_other.next
            if diff < 0:
                diff += 10
                borrow = -1
            else:
                borrow = 0
            result.digits.addLast(diff)
        result.sign = '+' if result.digits.head.data >= 0 else '-'
        return result

    @staticmethod
    def convert_to_linked_list(temp_result):
        result_linked_list = DoublyLinkedList()
        leading_zero = True
        for num in reversed(temp_result):
            if leading_zero and num == 0:
                continue
            leading_zero = False
            result_linked_list.addFirst(num)
        if result_linked_list.head is None: 
            result_linked_list.addFirst(0)
        return result_linked_list
    
    def __mul__(self, other): #if you looked at my d2l comment on my last submit i could not get this to work. i got it working now but had to add in some extra funtions. hope thats ok
        if not isinstance(other, bigNum):
            raise Exception("Operand must be a bigNum")
        result = bigNum()
        result.sign = '+' if self.sign == other.sign else '-'
        temp_result = [0] * (len(self.digits.to_list()) + len(other.digits.to_list()))
        for i, digit_self in enumerate(self.digits.to_list()):
            for j, digit_other in enumerate(other.digits.to_list()):
                temp_result[i + j] += digit_self * digit_other
                temp_result[i + j + 1] += temp_result[i + j] // 10
                temp_result[i + j] %= 10
        result.digits = bigNum.convert_to_linked_list(temp_result)

        return result

    
    def __div__(self, other): #i cannot figure out why this is not working, it has somthing to do with >=. ive tried stack, ai and reformating __div__ so many times
        if not isinstance(other, bigNum):
            raise Exception("Operand must be a bigNum")
        if other == bigNum('0'):
            raise ZeroDivisionError("Cannot divide by zero")
        result = bigNum()
        remainder = bigNum()  # Initialize remainder as a bigNum
        current = self.digits.head
        while current:
            remainder = remainder * bigNum('10') + bigNum(str(current.data))  # Convert current digit to bigNum and add to remainder
            result_digit = bigNum('0')  # Initialize result_digit as a bigNum
            while remainder > other:  # Loop until remainder is less than other
                remainder = remainder - other  # Subtract other from remainder
                result_digit = result_digit + bigNum('1')  # Increment result_digit by 1
            result.digits.addLast(result_digit)  # Add result_digit to result
            current = current.next
        result.sign = '+' if self.sign == other.sign else '-'  # Determine the sign of the result
        return result

    def __str__(self):
        current = self.digits.head
        output = '-' if self.sign == '-' and not (len(self) == 1 and self.digits.head.data == 0) else ''
        while current:
            output += str(current.data)
            current = current.next
        return output[::-1]


    def __len__(self):
        return len(self.digits)

    def __eq__(self, other):
        if not isinstance(other, bigNum):
            return False
        return self.sign == other.sign and self.digits == other.digits

    def __gt__(self, other):
        if not isinstance(other, bigNum):
            raise Exception("Operand must be a bigNum")
        if self.sign == '+' and other.sign == '-':
            return True
        elif self.sign == '-' and other.sign == '+':
            return False
        elif self.sign == '+':
            return len(self.digits) > len(other.digits) or self.digits > other.digits
        else:
            return len(self.digits) < len(other.digits) or self.digits < other.digits

    def __lt__(self, other):
        return not (self == other or self > other)


