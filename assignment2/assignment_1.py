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


english = validateInput("Enter Marks obtained out of 100 in English : ")
math = validateInput("Enter Marks obtained out of 100 in Math: ")
physics = validateInput("Enter Marks obtained out of 100 in Physics: ")
islamyat = validateInput("Enter Marks obtained out of 100 in Islamyat: ")
pakStudies = validateInput("Enter Marks obtained out of 100 in pakistan studies: ")
totalMarks = 500
totalGainedMarks = english + math + physics + islamyat + pakStudies
percentage = totalGainedMarks / totalMarks * 100

if (percentage < 40):
    grade = "F"
elif (percentage >= 40 and percentage < 50):
    grade = "D"
elif (percentage >= 50 and percentage < 60):
    grade = "C"
elif (percentage >= 60 and percentage < 70):
    grade = "B"
elif (percentage >= 70 and percentage < 80):
    grade = "A"
elif (percentage >= 80 and percentage <= 100):
    grade = "A+"
result = "|=========================================================| \n"
result +="|                       MarkSheet                         | \n"
result += "|=========================================================| \n"
result+="|Subject            total Marks            Obtained Marks |\n"
result += "|=========================================================| \n"
result+="|English             100                    {}            |\n".format(english)
result+="|Math                100                    {}            |\n".format(math)
result+="|Physics             100                    {}            |\n".format(physics)
result+="|Islamyat            100                    {}            |\n".format(islamyat)
result+="|PST             100                        {}            |\n".format(english)
result += "|=========================================================| \n"
result+="|Total               500         {} percentage({}) Grade ({})|\n".format(totalGainedMarks, percentage,grade)
print(result)