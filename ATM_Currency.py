amount = int(input("Enter the Amount to be withdrawn : "))

number_of_1000_notes=0
number_of_500_notes=0
number_of_100_notes=0

if amount%1000>=0:
    number_of_1000_notes = int(amount/1000)
    amount = amount-(number_of_1000_notes*1000)

if amount%500>=0:
    number_of_500_notes = int(amount/500)
    amount = amount-(number_of_500_notes*500)

if amount%100>=0:
    number_of_100_notes = int(amount/100)
    amount = amount-(number_of_100_notes*100)

if amount==0:
   print("Number of 1000 notes : ",number_of_1000_notes)
   print("Number of 500 notes : ",number_of_500_notes)
   print("Number of  100 notes : ",number_of_100_notes)

else:
   print("Enter the valid amount in Multiple of 100")
