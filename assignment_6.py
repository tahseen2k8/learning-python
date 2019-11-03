import argparse

# run this command python3 assignment_6.py --firstValue 10 --secondValue 20


parser = argparse.ArgumentParser(description='add arguments for commandline!')
parser.add_argument("--firstValue")
parser.add_argument("--secondValue")

args = parser.parse_args()
firstValue = args.firstValue
secondValue = args.secondValue

additionOfValue = int(firstValue) + int(secondValue)

print(additionOfValue)
