credit_card_info = input("Please enter your credit card information: ")

if credit_card_info.isdigit():
    print("You entered an integer.")
elif isinstance(credit_card_info, str):
    print("You entered a string.")
else:
    print("The entered data type is not recognized.")
