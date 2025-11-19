import recommendation_logic
#the main interaction with the user
def get_user_input():
    """
    1- Asking the user for the trip budget 
    2- Allowing the user to select trip types by numbers

    """

    # Welcome message
    print("========================================")
    print("🌍 Welcome to the Travel Planning Assistant!")
    print("Let's help you set up your trip details.")
    print("========================================\n")


    #1- Ask for budget
    while True:
        try:
            budget = int(input("Enter your expected trip budget (integer only): "))
            break
        except ValueError:
            print("❌ Error: Please enter a valid integer.\n")

    #2- Ask for Trip types selection by numbers
    valid_trip_types = ["Leisure", "Shopping", "Cultural", "Beach", "Adventure"] #depends on Fahad’s code

    print("\n🔹 Available Trip Types:")
    for i, t in enumerate(valid_trip_types, start=1):
        print(f"{i}. {t}")

    print("\n👉 Choose one or more types by number. Example: 1, 3, 5\n")

    while True:
        try:
            user_input = input("Enter your choice(s): ")

            # Split and convert to integers
            chosen_numbers = [int(num.strip()) for num in user_input.split(",")]

            # Validate range
            invalid_nums = [n for n in chosen_numbers if n < 1 or n > len(valid_trip_types)]
            if invalid_nums:
                raise ValueError(f"Invalid option(s): {invalid_nums}")

            # Convert numbers to types
            chosen_types = [valid_trip_types[n - 1] for n in chosen_numbers]
            break

        except ValueError as e:
            print(f"❌ Error: {e}")
            print("Please choose numbers only from the list above.\n")

    return budget, chosen_types


budget, trip_types = get_user_input()

print("\n✅ Inputs saved successfully!")
print(f"Budget: {budget}")#test
print(f"Trip Types Selected: {trip_types}") #test
recommendations = recommendation_logic.getting_destination(budget, trip_types)#to test recommendation logic file
