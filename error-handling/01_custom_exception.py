def brew_chai(flavor):
    if flavor not in ['masala', 'ginger', 'cardamom']:
        raise ValueError(f"Flavor '{flavor}' is not available. Please choose from 'masala', 'ginger', or 'cardamom'.")
    return f"Brewing a delicious cup of {flavor} chai!"

brew_chai('masala')  
brew_chai('vanilla')  # ValueError