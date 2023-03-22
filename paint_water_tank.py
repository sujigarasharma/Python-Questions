import math

radius = float(input("Enter the radius of the water tank in cm: "))
height = float(input("Enter the height of the water tank in cm: "))

surface_area = 2 * math.pi * radius * (radius + height)

cost = 0.02 * surface_area

print("The cost to paint the water tank is Rs. {:.2f}/-".format(cost))
