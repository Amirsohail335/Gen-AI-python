seat_type = input("enter the seat type (sleeper/AC/general/luxury)").lower()


match seat_type:
    case "sleeper":
        print("SLeeper simple to travel")
    case "AC":
        print("Include AC")
    case "general":
        print("General seats")
    case "luxury":
        print("Luxury seats") 
    case _:
        print("no matched")
