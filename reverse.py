Number = int(input("Please Enter any Number: "))
Reverse = 0
Sum=0
while (Number > 0):
    Reminder = Number % 10
    Sum=Reminder+Sum
    Reverse = (Reverse * 10) + Reminder
    Number = Number // 10

print("\n Reverse of entered number is = %d" % Reverse)
print("\n Sum of Number is = %d" %Sum)
