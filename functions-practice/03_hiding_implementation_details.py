# build simple app that register users
# sepearte concerns - getting_input, validate and save it
# write register_user() that calles - get_input(), validate_input(), save_to_db()

def get_input():
    print(f'Geting the input from the user!')

def validate_input():
    print(f'Validating the input!')

def save_to_db():
    print(f'Saving data to database.')

def register_user():
    get_input()
    validate_input()
    save_to_db()
    print(f'User is registered!')

register_user()