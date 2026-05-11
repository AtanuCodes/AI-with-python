seat_type = input("What is your preferred seat type? (Sleeper, AC, General or Luxury?): ").lower()

match seat_type:
    case 'sleeper': print("You have selected Sleeper class. The ticket price is $50.")
    case 'ac': print("You have selected AC class. The ticket price is $100.")
    case 'general': print("You have selected General class. The ticket price is $20.")
    case 'luxury': print("You have selected Luxury class. The ticket price is $150.")
    case _: print("Invalid seat type. Please choose from Sleeper, AC, General or Luxury.")