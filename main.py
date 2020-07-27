def getEquation(coordinate1, coordinate2):
    m = ((int(coordinate1[1]) - int(coordinate2[1])) / (int(coordinate1[0]) - int(coordinate2[0])))
    print(m * int((coordinate1[0])) + int(coordinate1[1]))


Coord1A = "1,1".split(",")
Coord1B = "3,3".split(",")

getEquation(Coord1A, Coord1B)

Coord2A = "-6,0".split(",")
Coord2B = "-4,-2".split(",")


line1M = 1
line1B = 2

line2M = -1
line2B = -6

AnsX = ((line1B - line2B) / (line2M - line1M))
AnsY = (line1M * AnsX + line1B)

print("({},{})".format(AnsX, AnsY))
