cup_size = input("Enter your cup size (small, medium, large): ").lower()
if cup_size == 'small':
    print("You have ordered a small cup of coffee which costs $2.50.")
elif cup_size == 'medium':
    print("You have ordered a medium cup of coffee which costs $3.00.")
elif cup_size == 'large':
    print("You have ordered a large cup of coffee which costs $3.50.")
else:
    print("Invalid cup size. Please choose from small, medium, or large.")