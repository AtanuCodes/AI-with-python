tea_price_bdt = {
    'Masala chai': 50,
    'Lemon tea': 100,
    'Ginger tea': 120
}

tea_price_usd = {tea: round(price/110, 2) for tea,price in tea_price_bdt.items()}
print(tea_price_usd)