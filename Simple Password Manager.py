pwd = (input("Type the master password: ")).lower()

pwd_dic = {}

def view(pwd_dic):
    pwd_ask = (input("Please give the master password to be able to see the data: ")).lower()
    if pwd_ask == pwd:
    # print(pwd_dic)
        for k, v in pwd_dic.items():
            print(k,v)

def add():
    pwd_ask = (input("Please give the master password to be able to add data: ")).lower()
    if pwd_ask == pwd:
        email = input('E-mail: ')
        new_pwd = (input('Type the password you want to save: ')).lower()
        # pwd_dic.update({email:new_pwd})
        pwd_dic[f"{email}"] = f'{new_pwd}'
        return pwd_dic
    else:
        print('The password is wrong.')

while True:
    mode = (input("To view the actuall saved passwords type 'view'. To add a new passoword tyoe 'add'. To quit type 'q': ")).lower()
    if mode == 'q':
        break

    if mode == 'view':
        view(pwd_dic)

    elif mode == 'add':
        add()

    else:
        print('Not a valid mode. Please give another mode or quit.\n')
        continue

    