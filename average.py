#def main():
 #   n = int(input("How many numbers do you have? "))
  #  sum = 0.0
   # for i in range(n):
    #    x = float(input("Enter a number >> "))
     #   sum = sum + x
    #print("\nThe average of the numbers is", sum / n)


def main():
    sum = 0.0
    count = 0
    moredata = "yes"
    while moredata[0] == "y":
        x = float(input("Enter a number >> "))
        sum = sum + x
        count = count + 1
        moredata = input("Do you have more numbers (yes or no)? ")
    print("\nThe average of the numbers is", sum / count)


if __name__ == '__main__':
    main()