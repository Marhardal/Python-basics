dicts = {"1": "one", "2": "two", "3": "three"}

print(type(dicts))

print(dicts)

print(dicts.keys())

print(dicts.values())

print(dicts["2"])

dicts["4"] = "four"

print(dicts)

dicts.pop("2")

print(dicts)

print("2" in dicts)

print("4" in dicts)

print("4" in dicts.values())

dicts["1"] = {"Name": "Martin", "Surname": "Harawa", "Gender": "Male"}

print("Martin" in dicts["1"].values())

print(dicts["1"]["Name"].upper())