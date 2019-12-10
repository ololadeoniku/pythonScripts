
# This program will compute the factorial of a whole number

def main():
    n = int(input("Please enter a whole number: "))
    factorial = 1
    for factor in range(n,1,-1):
       factorial = factorial * factor
    print("The factorial of", n, "is", factorial)

if __name__ == '__main__': main()
