snack = input("Enter your prefered snack:").lower()

if snack == "cookies" or snack == "samosa":
    print(f"we will serve you snack {snack}")
else:
    print("sorry we only serve somosa and cookies")

print(f"user said: {snack}")