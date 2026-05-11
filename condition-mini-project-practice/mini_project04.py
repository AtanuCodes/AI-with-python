device_status = 'off'
temperature = 45
if device_status == 'active' and temperature > 35:
    print("The temperature is high.")
elif device_status == 'active' and temperature < 30:
    print("The temperature is normal.")
else:
    print("Device is offline!")