# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

class Math():
    def __init__(self, ab, bc):
        self.ab = ab
        self.bc = bc

    def find_angle_MBC(self):
        hypotenuse = math.hypot(ab,bc)
        result = round(math.degrees(math.acos(bc/hypotenuse)))
        degree_sign = chr(176)
        print(str(result) + degree_sign)

if __name__ == '__main__':
    ab = int(input())
    bc = int(input())

    my_object = Math(ab, bc)
    my_object.find_angle_MBC()
