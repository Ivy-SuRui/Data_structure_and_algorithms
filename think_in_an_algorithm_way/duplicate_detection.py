# input: new individual's birthday, existing birthday list
# output: any repetition, true retrun pairs


# create a list to store input if no repetition
birthday_dict = {}

# check duplication
def has_duplicate_birthday(birthday_dict):
    # get each individual's birthday
    while True:
        name = input("What's your name? ")
        birthday = input("When is your birthday? ")
    # compare input with my list to see if repeated
        if birthday in birthday_dict:
            # if repeated return pair
            print(f"Duplication found. {name} is also on the birthday {birthday} with {birthday_dict[birthday]}.")
            break
        # if not store the input into the list and move to the next input until the end
        else:
            birthday_dict[birthday] = name
            print("No duplication found. Move on to the next individual.")

        
has_duplicate_birthday(birthday_dict)


