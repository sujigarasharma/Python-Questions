h, m, s = map(int, input("Enter the current time in hours, minutes, and seconds (separated by spaces): ").split())
s1 = int(input("Enter the number of seconds to add: "))

total_s = h*3600 + m*60 + s + s1

new_h = total_s // 3600
new_m = (total_s % 3600) // 60
new_s = (total_s % 3600) % 60

print("New time after adding {} seconds: {} hours {} minutes {} seconds".format(s1, new_h, new_m, new_s))
