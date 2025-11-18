# A constant that stores the current year for calculating the user's age
CURRENT_YEAR = 2025


def generate_profile(age):
    """Determine the user's "life stage" based on their age.

    Args:
        age (int): The user's age.

    Returns:
        str: The user's life stage.
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    else:
        return "Adult"


def get_current_age(birth):
    """Determine the user's age.

    Args:
        birth (int): The user's birth year.

    Returns:
        int: The user's current age.
    """
    return CURRENT_YEAR - birth


def get_hobby():
    """Determine the user's hobby.

    Prompts the user to enter a hobby and returns the entered string, or None if the user entered "stop"

    Returns:
        str or None: The user's hobby.
    """
    input_str = input("Enter a favorite hobby or type 'stop' to finish: ").strip()

    return None if input_str.lower() == "stop" else input_str


def print_user_profile(profile):
    """Print the user's profile.
D
    Args:
        profile (dict): The user's profile.
    """
    name = profile["name"]
    age = profile["age"]
    stage = profile["stage"]
    hobbies_list = profile["hobbies"]

    print("\n---")
    print("Profile Summary:")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Life stage: {stage}")

    if hobbies_list:
        print(f"Favorite Hobbies ({len(hobbies_list)}):")

        for item in hobbies_list:
            print(f"- {item}")
    else:
        print("You didn't mention any hobbies.")

    print("---")


# Get user's input (name and birth_year)
user_name = input("Enter your full name: ")
birth_year_str = input("Enter your birth year: ")
birth_year = int(birth_year_str)

current_age = get_current_age(birth_year)

hobbies = []

# Loop for repeatedly asking the user to enter a hobby
while True:
    hobby = get_hobby()

    if hobby is None:
        break

    hobbies.append(hobby)

life_stage = generate_profile(current_age)

# Stores all collected user's information (name, age, stage and hobbies list)
user_profile = {
    "name": user_name,
    "age": current_age,
    "stage": life_stage,
    "hobbies": hobbies
}

print_user_profile(user_profile)
