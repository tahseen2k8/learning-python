import argparse

# run this command python3 assignment_5.py --firstName Mohammed --lastName Tahseen



parser = argparse.ArgumentParser(description='add arguments for commandline!')
parser.add_argument("--firstName")
parser.add_argument("--lastName")


def reverse_list(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)


args = parser.parse_args()
firstName = args.firstName
lastName = args.lastName
print("here is the reverse order of your name=> {} {}".format(reverse_list(firstName),reverse_list(lastName)))

