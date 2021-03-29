daily_profit = int(input(“Enter Daily Profit: “))
time = int(input(“How many days: “))
deposit = int(input(“How much is your deposit?: “))
time_zero = 1
while time_zero <= time:
  deposit = deposit*(100 + daily_profit)/100
  time_zero += 1
print (‘Your new deposit is {:.2f} $’.format (deposit))
