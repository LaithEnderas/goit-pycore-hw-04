def parse_input(user_input):
    cmd, *args = user_input.split()                              # split input into command and arguments
    cmd = cmd.strip().lower()                                    # convert to lowercase for case insensitivity
    return cmd, *args

def add_contact(args, contacts):                                 # extract name and phone number from args and add to dictionary
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):                              # extract name and phone number from args and update dictionary
    name, phone = args
    contacts[name] = phone
    return "Contact changed."

def show_phone(args, contacts):                                  # extract name from args and look up phone number in dictionary
    name = args[0]
    if name in contacts:
        return contacts[name]
    else:
        return None

def show_all(args, contacts):                                    # show all contacts in dictionary
    return contacts

def main():
    contacts = {}                                                # create new clean dictionary
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
                                                                 # commands block
        if command in ["close", "exit"]:                         
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            result = show_phone(args, contacts)
            if result is not None:
                print(f'Phone number for contact {args[0]}: {result}')
            else:
                print('Contact not found.')
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
