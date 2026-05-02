from collections.abc import Callable


def input_error(func: Callable) -> Callable:
    def inner(*args: list, **kwargs: dict) -> str:
        try:
            return func(*args, **kwargs)
        except KeyError:
            return 'This contact not exist, choose another one'
        except ValueError:
            return 'Please give me name and phone number'
        except IndexError:
            return 'Please give me name you looking for'
        except Exception:
            return 'Something went wrong, please try again'
    return inner


@input_error
def parse_input(user_input: str) -> tuple:
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args


@input_error
def add_contact(args: list, contacts: dict) -> str:
    name, phone = args
    if name in contacts:
        return (
            f'Contact "{name}" already exists. If you want to change\
            the phone number, use the "change" command.'
        )
    contacts[name] = phone
    return 'Contact added.'


@input_error
def change_contact(args: list, contacts: dict) -> str:
    name, phone = args
    contacts[name] = phone
    return 'Contact updated.'


@input_error
def show_phone(args: list, contacts: dict) -> str:
    name = args[0]
    return contacts[name]


@input_error
def show_all(contacts: dict) -> str:
    return '\n'.join(f' {name}: {phone}' for name, phone in contacts.items())


def help():
    commands = [
        'help','hello',
        'add {name} {phone}',
        'change {name} {phone}',
        'phone {name}',
        'show {name}', # alias for 'phone'
        'all', 'close', 'exit',
    ]
    return 'Available commands:\n  ' + '\n  '.join(commands)


def main():
    contacts = {}
    print('Welcome to the assistant bot!')

    while True:
        user_input = input('Enter a command: ')
        command, *args = parse_input(user_input)

        if command in ['close', 'exit']:
            print('Good bye!')
            break
        elif command == 'hello':
            print('How can I help you?')
        elif command == 'add':
            print(add_contact(args, contacts))
        elif command == 'change':
            print(change_contact(args, contacts))
        elif command in ['show', 'phone']:
            print(show_phone(args, contacts))
        elif command == 'all':
            print(show_all(contacts))
        elif command == 'help':
            print(help())
        else:
            print(
                f'Іnvalid command.'
                'Type "help" to see the list of available commands.'
            )


if __name__ == '__main__':
    main()
