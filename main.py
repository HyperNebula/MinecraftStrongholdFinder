line1M = 1
line1B = 2

line2M = -1
line2B = -6

AnsX = ((line1B - line2B) / (line2M - line1M))
AnsY = (line1M * AnsX + line1B)

print("({},{})".format(AnsX, AnsY))
