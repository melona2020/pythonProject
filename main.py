Calculation_to_units = 24*60
name_of_unit = "Minutes"


def days_to_unit(num_of_days):
    return f"{num_of_days} days are {num_of_days * Calculation_to_units} {name_of_unit}"


def validate_and_execute():
    if user_input.isdigit():
        user_input_number = int(user_input)
        if user_input_number > 0:
            calculated_value = days_to_unit(user_input_number)
            print(calculated_value)
        elif user_input_number == 0:
            print("you entered 0 please enter a positive number")
    else:
        print("User input is invalid Please try again with integer value")


user_input = input("Hey User, Please enter number of days? I will calculate how many Minutes!\n")
validate_and_execute()
