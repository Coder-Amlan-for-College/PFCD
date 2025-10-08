room_type = input("Enter the room type(Standard,Deluxe,Suite): ")
length_of_stay = int(input("Enter the length of stay: "))
season = input("Season(Peak or Off): ")
loyalty_mem = input("Loyalty member:(y or n): ")
if room_type.lower() == "standard":
    cost_per_night = 100
elif room_type.lower() == "deluxe":
    cost_per_night = 150
elif room_type.lower() == "suite":
    cost_per_night = 250

if season.lower()=="peak":
    cost_per_night = cost_per_night+cost_per_night*0.2
elif season.lower()=='off':
    cost_per_night = cost_per_night-cost_per_night*0.15

dis = 0.0
if length_of_stay>3:
    dis = 0.1
elif length_of_stay>7:
    dis = 0.2



    