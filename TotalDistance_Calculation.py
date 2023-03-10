x = float(input("Enter the speed of the car in km/h from start to point A: "))
h1 = int(input("Enter the starting hour (in 24 hour format): "))
m1 = int(input("Enter the starting minute: "))
h2 = int(input("Enter the ending hour (in 24 hour format): "))
m2 = int(input("Enter the ending minute: "))
y = float(input("Enter the speed of the car in km/h from point A to point B: "))
h3 = int(input("Enter the starting hour (in 24 hour format): "))
m3 = int(input("Enter the starting minute: "))
h4 = int(input("Enter the ending hour (in 24 hour format): "))
m4 = int(input("Enter the ending minute: "))

start_time = h1 + m1/60
end_time1 = h2 + m2/60
start_time2 = h3 + m3/60
end_time2 = h4 + m4/60

distance1 = (end_time1 - start_time) * x
distance2 = (end_time2 - start_time2) * y

total_distance = distance1 + distance2

print("The total distance covered by the car is", total_distance, "km")
