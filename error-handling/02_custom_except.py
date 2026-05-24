class customChaiError(Exception):
    """Custom exception for invalid chai flavors."""
    pass

def make_chai(milk, suger):
    if milk not in ['whole', 'skim', 'almond']:
        raise customChaiError(f"Milk type '{milk}' is not available. Please choose from 'whole', 'skim', or 'almond'.")
    if suger not in ['white', 'brown', 'honey']:
        raise customChaiError(f"Sugar type '{suger}' is not available. Please choose from 'white', 'brown', or 'honey'.")
    return f"Making chai with {milk} milk and {suger} sugar."

# print(make_chai('whole', 'white'))
print(make_chai('soy', 'white'))  # customChaiError