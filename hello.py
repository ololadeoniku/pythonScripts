# print("HelloWorld again")
# print("great!!!")
# for number in range(6):
#     print("*"*(number+1))

# for number2 in range(1,7):
#     print(f"{(6-number2)*' '} {'*'*number2}")

# '''counter = 0
# for x in range(1,10):
#     if x % 2 == 0:
#         print(x)
#         counter = counter + 1
# print(f"We have ourselves {counter} even numbers")'''


# def even_numbers(*numbers):
#     counter = 0
#     for number in numbers:
#         if number % 2 == 0:
#             print(number)
#             counter += 1
#     print(f"we have {counter} even numbers")


# even_numbers(1,2,3,5,6,8,9,15,16,19,24)

# while True:
#     command = input(">>> ")
#     if command.lower() == "quit":
#         break

#Fizz-Buzz problem, takes an return Fizz when input divisible by 3, return Buzz if by 5, return input if not divisible by either 3 or 5

class FB:
    
    def __init__(self, user):
        self.user = user
        self.convertUser = int(user)
        
    def get_input(self):
        number = self.convertUser
        return number

    def is_divisible_by3(self):
        if self.get_input() % 3 == 0:
            return True

    def is_divisible_by5(self):
        if self.get_input() % 5 == 0:
            return True

    def is_divisible_by3or5(self):
        if self.get_input() % 3 == 0 and self.get_input() % 5 == 0:
            return True

    def print_output(self):
        if self.is_divisible_by3() and self.is_divisible_by5():
            print("FizzBuzz")
        if self.is_divisible_by5() and not self.is_divisible_by3():
            print("Buzz")
        if self.is_divisible_by3() and not self.is_divisible_by5():
            print("Fizz")
        if not self.is_divisible_by3() and not self.is_divisible_by5():
            print(self.get_input())
while True:
    user = input("please enter a number to check >> ")
    if user.lower() == "exit":
        break
    FB(user).print_output()









