import math
def input_x():
    x = int(input("Faka ikho-odineyithi ka x"))
    return x
def input_y():
    y = int(input("Faka ikho-odineyithi ka y"))
    return y
def input_radius():
    radius = int(input("Faka irediyasi"))
    return radius
def calc_perimeter(r):
    perimeter = 2 * (3.14 * r)
    print("Ipherimitha yesekile", perimeter)

def calc_area(r):
    area = 3.14 * (r * r)
    print("I-Eriya yesekile", area)

def insideoutsidecircle(x, y, r):
    distance = math.sqrt((x-0) * (x-0) + (y-0)*(y-0))
    if distance< r:
        print("Ipoyinti ingaphandle kwesekile")
    else:
        print("Ipoyinti ingaphakathi kwesekile")

if __name__ == '__main__':
    a = input_x()
    f = input_y()
    g = input_radius()
    calc_perimeter(g)
    calc_area(g)
    insideoutsidecircle(a, f, g)