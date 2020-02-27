def collect_phone_number():
    phoneNumber = input("type in your number: ").strip()
    while not phoneNumber.isdigit() or len(phoneNumber) !=11:
        print('Invalid Phone number')
        phoneNumber = input("type in your number: ").strip()

    return phoneNumber

def collect_name():
    name = input("type your name[ or q to quit ]: ").strip().lower()
    while not name.isalpha():
        print('Invalid Name!')
        name = input("type your name[ or q to quit ]: ").strip().lower()

    return name

def storeContact():
    global contacts
    contacts = {}

    while True:
        name = collect_name()
        if name == 'quit' or name ==  'q':
            break
        phoneNumber = collect_phone_number()

        contacts[name] = phoneNumber

def retrieveContact():
    while True:
        name = collect_name()
        if name == 'quit' or name ==  'q':
            break
        try:
            print(name, contacts[name])
        except:
            print('Key does not exist')

def main():
    print('STORAGE MODE')
    storeContact()
    print(contacts)

    print('\n RETRIVAL MODE')
    retrieveContact()


if __name__ == '__main__':
    main()

