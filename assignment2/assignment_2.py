#Write a program which take input from user and identify that the given
#number is even or odd?

def validateInput(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Please enter Integer value! Try again.")
            continue
        else:
            return userInput
            break


number  = validateInput("Enter Numer to validate : ")

if (number % 2) == 0:
   print("{0} is Even number".format(number))
else:
   print("{0} is Odd number".format(number))
