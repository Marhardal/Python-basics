year = int(input("Enter your birth year: "))

def getuserage(year):
    """
    Calculate the age of a user based on their birth year.
    """
    from datetime import datetime
    current_year = datetime.now().year
    age = current_year - year
    return age

print(f"You are {getuserage(year)} years old.")