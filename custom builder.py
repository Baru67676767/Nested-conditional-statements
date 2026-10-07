print("--------------------")
print(" Welcome to Ride Builder! ")
print("--------------------")
print()
print("Step 1: Pick your vehicle")
print(" 1 - Bike")
print(" 2 - Car")
print()
choice = int(input("Enter 1 or 2: "))
print()


if choice == 1:
# Nested if-else - runs only when choice is 1
    print("Step 2: Pick your bike type")
    print(" 1 - Scooty")
    print(" 2 - Mountain Bike")
    print()

    bike_type = int(input("enter 1 or 2:"))
    print()

    if bike_type == 1:
        print("you picked : scooty")
        print(" top speed  ; 80km/h")
        print("best for  : city roads")
    else:
        print("you picked :mountain bike")
        print("top speed  : 40km/h")
        print("best for  : off-road trails")

elif choice == 2:
# Nested if-else - runs only when choice is 2
        print("Step 2: Pick your car type")
        print(" 1 - sedan")
        print("2 - SUV")
        print()

        car_type = int(input("enter 1 or 2:"))
        if car_type == 1:
                    print("you picked : sedan")
                    print("seats       : 5 passengers")
                    print("best for   : family trips")
        else:
            print("you picked  :SUV")
            print("seats  :7 passengers")
            print("best for  : off-road adventures")

    
else:
        print("that was not a valid choice")
        print("please enter 1 for bike or 2 for car.")

        print()
        print("----------------------------------------")
print(" Thank you for using Ride Builder! ")
print("----------------------------------------")

    
             
    