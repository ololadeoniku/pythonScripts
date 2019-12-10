#


def main():
    print("This program calculates the future value of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate in decimal, for example 8% will be 0.08: "))

    for i in range(10):
       principal = principal * (1 + apr)

    print ("The value in 10 years is:", principal)
main()
