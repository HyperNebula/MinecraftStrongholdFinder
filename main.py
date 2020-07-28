def getEquation(coordinate1, coordinate2):
    m = ((int(coordinate1[1]) - int(coordinate2[1])) / (int(coordinate1[0]) - int(coordinate2[0])))
    b = m * -int((coordinate1[0])) + int(coordinate1[1])
    return (m,b)


Coord1A = "1,1".split(",")
Coord1B = "3,3".split(",")

(line1M,line1B) = getEquation(Coord1A, Coord1B)

Coord2A = "0,6".split(",")
Coord2B = "6,0".split(",")

(line2M,line2B) = getEquation(Coord2A, Coord2B)

AnsX = ((line1B - line2B) / (line2M - line1M))
AnsY = (line1M * AnsX + line1B)

print("({},{})".format(AnsX, AnsY))
