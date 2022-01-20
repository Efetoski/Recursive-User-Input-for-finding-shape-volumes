import math

def Sphere(r):
    volume = (3/4) * math.pi * r**3
    return volume

def Cone(r,h):
    volume = math.pi * r**2 * (h/3)
    return volume

def Cylinder(r,h):
    volume = math.pi * (r**2) * h
    return volume

def shape():
    while True:
        option = int(input("Please type 1 for sphere, 2 for cylinder and 3 for cone: "))
        if option == 1:
            r = int(input("Enter the radius of the Sphere: "))
            volume = Sphere(r)
            print(volume)

        elif option == 2:
            r = int(input("Enter the radius of the Cone: "))
            h = int(input("Enter the height of the Cone: "))
            volume = Cone(r,h)
            print(volume)

        elif option == 3:
            r = int(input("Enter the radius of the Cylinder: "))
            h = int(input("Enter the height of the Cylinder: "))
            volume = Cylinder(r,h)
            print(volume)

        else:
            print("Invalid Option!!!")
shape()
