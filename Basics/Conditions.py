from datetime import datetime

by = input("Enter birth year: ")
isold = datetime.now().year - int(by) >= 18

if isold:
    print("You are old enough to drive.")
else:
    years_to_wait = 18 - (datetime.now().year - int(by))
    print(f"You are not old enough to drive. You need to wait for {years_to_wait} years.")