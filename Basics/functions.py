year = int(input("Enter your birth year: "))

def getuserage(year):
    from datetime import datetime
    current_year = datetime.now().year
    age = current_year - year
    return age

print(f"You are {getuserage(year)} years old.")