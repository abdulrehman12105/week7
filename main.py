NUM_CHARITIES = 3
DONATION_PERCENTAGE = 0.01

# Initialize charity names and donation totals
charity_names = []
charity_totals = [0] * NUM_CHARITIES

# Get charity names
for i in range(1, NUM_CHARITIES + 1):
    charity_name = input(f"Enter the name of Charity {i}: ")
    charity_names.append(charity_name)

# Function to validate charity choice
def validate_charity_choice(choice):
    return -1 <= choice <= NUM_CHARITIES

# Function to record and total each donation
def record_and_total_donation():
    while True:
        # Get customer's charity choice
        charity_choice = int(input(f"\nEnter the number (1-{NUM_CHARITIES}) for the chosen charity, or -1 to show totals: "))

        # Validate charity choice
        if validate_charity_choice(charity_choice):
            # Check if the user wants to show totals
            if charity_choice == -1:
                show_totals()
                break

            # Get customer's shopping bill
            shopping_bill = float(input("Enter the customer's shopping bill amount: "))

            # Calculate donation amount
            donation_amount = shopping_bill * DONATION_PERCENTAGE

            # Update total donation for the chosen charity
            charity_totals[charity_choice - 1] += donation_amount

            # Display donation details
            print(f"\nDonation Details:")
            print(f"Chosen Charity: {charity_names[charity_choice - 1]}")
            print(f"Donation Amount: ${donation_amount:.2f}")

        else:
            print("Error: Invalid charity choice. Please choose a number within the specified range.")

# Function to show the totals
def show_totals():
    # Create a list of tuples (charity_name, charity_total)
    combined_data = list(zip(charity_names, charity_totals))

    # Sort the list in descending order of totals
    combined_data.sort(key=lambda x: x[1], reverse=True)

    # Display the totals in descending order
    print("\nTotals So Far (Descending Order):")
    grand_total = 0
    for name, total in combined_data:
        print(f"{name}: ${total:.2f}")
        grand_total += total

    # Display the grand total
    print(f"\nGRAND TOTAL DONATED TO CHARITY: ${grand_total:.2f}")

# Call the function to record and total each donation
record_and_total_donation()
