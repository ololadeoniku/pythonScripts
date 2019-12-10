

import math
#quadraticroot.py
#Program to compute the roots of a quadratic equation

def main():
    print("Hi and Welcome. We are happy to compute the roots of your quadratic equation")   #Welcome message
    print("Just enter the values of the coefficients and press enter to see the result")
    print()
    a = int(input("My wife wants you to Enter the coefficient of the first term: "))   #first coefficeint goes here
    b = int(input("My wife wants you to Enter the coefficient of the second term: "))  #second coefficient goes here
    c = int(input("My wife wants you to enter the value of constant term: "))          # constant term goes here
    print()
    denom = 2*a                                                 # value of denominator of quadratic equation
    numer1 = -1*b                                                # value of the first term of numerator in equation
    subt_term = (b*b) - (4*a*c)
    if subt_term >= 0:
        numer2 = math.sqrt((b * b) - (4 * a * c))  # value of second term of numerator
        x1 = (((numer1 + numer2) / denom))
        x2 = (((numer1 - numer2) / denom))
        print("The real roots of your quadratic equation are: {0:0.2f} and {1:0.2f}".format(x1,x2))
        print()
        print("My wife and I thank you for using our program")
        print();
    else:
        print("The roots of your equation are complex roots, this program computes real roots. Please try again")



main()
