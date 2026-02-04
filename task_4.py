def parse_input(user_input):
    """
    Parses the user input into a command and arguments.
    """
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    """
    Adds a new contact or updates an existing one.
    Usage: add [name] [phone]
    """
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    """
    Updates the phone number for an existing contact.
    Usage: change [name] [new_phone]
    """
    name, phone = args[0]
    if name in contacts:
        contacts[name] = phone
        return "Contact updated."
    else:
        return f"Error: Contact '{name}' not found."

def show_phone(args, contacts):
    """
    Shows the phone number for a specific contact.
    Usage: phone [name]
    """
    name = args[0]
    if name in contacts:
        return contacts.get(name)
    else:
        return f"Error: Contact '{name}' not found."
    

def show_all(contacts):
    """
    Displays all saved contacts.
    Usage: all
    """
    heared = f'{'Name':<15} | {'Phone':<15}'
    separator = '-' * len(heared)

    show_all = [heared, separator]

    for name, phone in contacts.items():
        show_all.append(f'{name:<15} | {phone:<15}')
        
    return '\n'.join(show_all)

def main():
    """
    Main loop for the assistant bot.
    """
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

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
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
