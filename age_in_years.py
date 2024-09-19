def calculate_age(birth_year):
    from datetime import datetime

    current_year = datetime.now().year  # Get the current year
    age = current_year - birth_year
    return age

# Get user input
try:
    birth_year = int(input("Enter your birth year (e.g., 1990): "))
    if birth_year < 0:
        print("Year of birth cannot be negative.")
    else:
        age = calculate_age(birth_year)
        print(f"You are {age} years old.")
except ValueError:
    print("Please enter a valid year.")
    