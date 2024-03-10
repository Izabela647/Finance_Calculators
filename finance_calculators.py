import math
# Display a separator line for better visual separation
print ('-'*100)

# This is an example of Python program showing if-elif-else statements.
# Main loop to keep the program running until explicitly stopped
while True:
    # Provide options for the user to choose from
    print("Investment - to calculate the amount of interest you'll earn on your investment\n\
Bond - to calculate the amount you'll pay on a home loan \n\
                 ")
    # Get user input and convert it to lowercase for case-insensitivity
    invest_or_bond = input(str("Please enter Investment or Bond:\n" )).lower()
    print ('-'*100)

    if invest_or_bond == 'investment':  #Checks for valid entries.
        print("Chosen Investment Calculator")
        initial_deposit = float(input("Please enter the amount of money you are depositing\nR"))
        interest_rate = float(input("At which interest rate percentile?\n" ))
        r = interest_rate/100
        num_of_years = float(input("Please enter the number of years you plan on investing: \n"))
        INTEREST_TYPE = str(input("Would you prefer 'Simple' or 'Compound' interest. \n")).lower()

        # Prompting input from user to be able to perform desired calculation.

        # Perform the selected interest calculation
        if INTEREST_TYPE == "simple":
            result = initial_deposit*(1 + r * num_of_years)
        elif INTEREST_TYPE == "compound":
            results = initial_deposit * (1 + r) ** num_of_years
        else:
            # Raise an error if an invalid interest type is entered
            raise ValueError("Invalid interest type selected")

        print(f"Your interest earned over {num_of_years} years will be R{result if INTEREST_TYPE == 'simple' else results:.2f}")
        # Printing a formatted f-string outcome to user rounded to two decimal places.


    elif invest_or_bond == 'bond':  # Checks for valid entries.
        print("Chosen home loan repayment calculator")
        house_value = float(input("What is the current value of the house?\n"))
        i = float(input("At which interest rate percentile?\n" )) / 100 / 12
        num_of_months = float(input("Enter number of months you plan to repay the bond:? \n"))
    # Prompting input from user to be able to perform calculation.

        # Calculate the monthly repayment amount
        total = house_value * ((i * ((1 + i) ** num_of_months)) / (((1 + i) ** num_of_months) - 1))
        print(f"Your monthly repayment will be R{total:.2f}")
        # Display the monthly repayment amount rounded to two decimal places
    else:
        # Raise an error if an invalid menu option is entered
        raise ValueError ("Invalid menu option selected")
    
