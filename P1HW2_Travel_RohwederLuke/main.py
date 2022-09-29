#P1HW2_Travel
#9-29-2022
#CTI-110 P1HW2-Travel Expense
#Luke Rohweder

#inputs
print("This program calculates and displays travel expenses")
budget = float(input("Enter budget: $"))
travelDestination = input("Enter your tavel Destination: ")
gas = float(input("How much do you think you will spend on gas?: $"))
hotel = float(input("Approximately, how much will you need for accomodation/hotel?: $"))
food = float(input("What are your food costs?: $"))

print("-------------Travel Expenses---------------")
#outputs
print("Location:", travelDestination)
print("Initial Budget:", budget, "\n")

print("Fuel: $", gas)
print("Accomodation: $", hotel)
print("Food: $", food, "\n")

remainingAmount = budget-gas-hotel-food
print("Remaining Balance: $", remainingAmount)


