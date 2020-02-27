contacts = {}
print('STORAGE MODE')

while True:
    name = input("type in your name[ or q to quit ]: ").strip().lower()
    if name == 'quit' or name ==  'q':
        break
    phoneNumber = input("type in your number: ").strip()
    while not phoneNumber.isdigit() or len(phoneNumber) !=11:
        print('Invalid Phone number')
        phoneNumber = input("type in your number: ").strip()

    contacts[name] = phoneNumber
print(contacts)

print('\n RETRIVAL MODE')
while True:
    name = input("type in your name to check contacts[ or q to quit ]: ").strip().lower()
    if name == 'quit' or name ==  'q':
        break
    try:
        print(name, contacts[name])
    except:
        print('Key does not exist')
