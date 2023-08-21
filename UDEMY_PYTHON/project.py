# ---->>>> Greeting Project <<<<-----
# WAP that input to prompt a user for their name & then welcome them.

name=input("Enter your name: ")
print(f'Hello {name}.')
print(f'Welcome to the Python\n\n')

# ------------ PROJECT 2: -----------------
# ------>>>>> Group Name Generator <<<<------
#     1. Create a gretting to the program.
#     2. Ask the user to their favourite color.
#     3. Ask the user to the favourite animal.
#     4. Combine the name of their favourite color and animal and show them their group.

print("Welcome to the Group Name Generator.")
color=input("What's your favourite color?\n").capitalize()
animal=input("What's your favourite animal?\n").capitalize()
print(f"Your group name could be {color} {animal}s\n\n")

# ------------ PROJECT 3: -----------------
# ------>>>>> Gross Pay <<<<------
    # WAP to prompt the user for hours and rate per hour 
    # to compute gross pay.You need to take into account that 
    # result that exactly two digit after the decimal.

hours=int(input("Enter Hours: "))
rate=float(input("Enter Rate: "))
gross_pay=hours*rate
print("Pay:",round(gross_pay,2),'\n\n')

# ------------ PROJECT 4: -----------------
# ------>>>>> Celsius to Fahrenheit <<<<------
    # WAP which prompts the user for a Celsius temperature,convert the temperature to Fahrenheit,and print out the converted temperature.
    # Formula:
    #         (C*9/5)+32=F

Celsius=int(input("Enter Temperature in Celsius: "))
Fahren=(Celsius*9/5)+32
print(f"{Celsius} Celsius = {Fahren} Faherenheit \n\n")

# ------------ PROJECT 5: -----------------
# ------>>>>> Tip Cost Calculator <<<<------
    # WAP which calculates trip cost for a user.
    # 1. Create a greeting for your program.
    # 2. Ask the user for number of days.
    # 3. Ask the user for hotel price.
    # 4. Ask the user for flight price.
    # 5. Ask the user for rental car price.
    # 6. Ask for other expenses.
    # 7. Combines all expenses together and print with 2 digits after decimal places.

print("Welcome to the trip Cost Calculator!")
day=int(input("How many days will you stay? "))
hotel_price=float(input("How much does hotel cost per night? $"))
flight_price=float(input("How much flight cost? $"))
car_price=float(input("If you need rental car please enter the price otherwise enter zeros. $"))
other_expenses=float(input("Enter other possible expenses $"))
Cost=(day*hotel_price)+(day*car_price)+flight_price+other_expenses
print(f"Total cost: ${round(Cost,2)}") 