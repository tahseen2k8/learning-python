import math,argparse
# run this example please hit python3 assignment_4.py --radius 6
parser = argparse.ArgumentParser(description='add arguments for commandline!')
parser.add_argument("--radius")
args = parser.parse_args()
radius = args.radius
# as we know area = A=pi r^{2}


result = math.pow(int(radius),2)
somepi = math.pi * result

print("area of the circle by given radius is {}".format(somepi))