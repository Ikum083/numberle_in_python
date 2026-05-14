# import random module
import random as rnd

# class for generating the equation
class Equation:
    def generate_equation(self, number) -> str:
        equations = ["+", "-", "*", "/"]

        # quantity of numbers to be used excluding the total
        ##quantity_of_numbers = rnd.randint(2, 3)
        quantity_of_numbers = 2

        # condition where the quantity of numbers is only 2
        if quantity_of_numbers == 2:
            operation = rnd.choice(equations)
            print(operation)

            # condition if operation is addition
            while operation == "+":
                first_number = rnd.randint(1, number//2)
                second_number = number - first_number
                print("Addition")
                return f"{str(first_number).zfill(2)}+{str(second_number).zfill(2)}={str(number).zfill(2)}"
            
            # condition if operation is subtraction
            while operation == "-":
                first_number = rnd.randint(1, number//2)
                second_number = number + first_number
                print("Subtraction")
                return f"{str(second_number).zfill(2)}-{str(first_number).zfill(2)}={str(number).zfill(2)}"
            
            # condition if operation is multiplication
            while operation == "*":
                print("Multiplication")
                factors = []
                # while condition to check if number is odd or even to make it easier to detect prime numbers
                while number % 2 != 0:
                    # for loop the iterates through 1 to half of the total
                    for j in range(1, number // 2):
                        if number % j != 0:
                            continue
                        else:
                            factors.append(j)
                    # if the total is prime we restart 
                    if len(factors) == 0:
                        number = rnd.randint(1, 99)
                        continue
                    else:
                        first_number = rnd.choice(factors)
                        second_number = number / first_number
                        return f"{str(first_number).zfill(2)}*{str(second_number).zfill(2)}={str(number).zfill(2)}"

                # if nummber is even we simply find an even number to be the first factor
                else:
                    first_number = rnd.choice(range(1, 9, 2))
                    # if not divisible then we regenerate a number
                    if number % first_number != 0:
                        first_number = rnd.choice(range(1, 9, 2))
                    else:
                        second_number = int(number / first_number)
                        return f"{str(first_number).zfill(2)}*{str(second_number).zfill(2)}={str(number).zfill(2)}"
            
            # condition if the operation is division
            while operation == "/":
                print("Division")
                dividing = True
                while dividing:
                    first_number = rnd.randint(1, 9)
                    # condition where the first number is not divisible to the total so we restart until the first number is divisible
                    if number % first_number != 0:
                        first_number = rnd.randint(1, 9)
                        continue
                    else:
                        second_number = number * first_number
                        if len(str(second_number)) == 2:
                            return f"{str(second_number).zfill(2)}/{str(first_number).zfill(2)}={str(number).zfill(2)}"
                        else:
                            return f"{second_number}/{first_number}={number}"