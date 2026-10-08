device_status = "active"
temperature = 49


if device_status == "active":
    if temperature >35:
        print("Warm")
    else:
        print("normal temp")
    
else:
    print("Device is offline")


