from os import system
system('cls')
class info:
    def __init__(self):
        self.__id = 0
        self.__name = 'no name'
        self.__CodeCity = '000'
        self.__phone = '00000000'
        self.__adress = 'no adress'
        self.__email = 'no email'
    def __str__(self):
        return f'{self.__id}\t{self.__name}\t{self.__CodeCity} {self.__phone}\t{self.__adress}\t{self.__email}'
    @property
    def ID(self):
        return self.__id
    @ID.setter
    def ID(self, code):
        self.__id = code
    @ID.deleter
    def ID(self):
        print(f"deleted:{self.__id}", end='')
        del self.__id

    @property
    def Name(self):
        return self.__name
    @Name.setter
    def Name(self,fname):
        self.__name = fname
    @Name.deleter
    def Name(self):
        print(f"deleted: {self.__name}")
        del self.__name

    @property
    def phone_number(self):
        return self.__phone
    @phone_number.setter
    def phone_number(self,Phone):
        self.__phone = Phone
    @phone_number.deleter
    def phone_number(self):
        print(f"deleted {self.__phone}")
        del self.__phone

    @property
    def code_city(self):
        return self.__CodeCity
    @code_city.setter
    def code_city(self,Code):
        self.__CodeCity = Code
    @code_city.deleter
    def code_city(self):
        del self.__CodeCity

    @property
    def home_adress(self):
        return self.__adress
    @home_adress.setter
    def home_adress(self,hadress):
        self.__adress = hadress
    @home_adress.deleter
    def home_adress(self):
        print(f"deleted {self.__adress}")
        del self.__adress

    @property
    def Email(self):
        return self.__email
    @Email.setter
    def Email(self,mail):
        self.__email = mail
    @Email.deleter
    def Email(self):
        print(f"deleted {self.__email}")
        del self.__email
class Haghighi(info):
    def __init__(self):
        super().__init__() 
        self.__real_name = 'no real names'
        self.__family_members = 'no family members'
    @property
    def real_name(self):
        return self.__real_name

    @real_name.setter
    def real_name(self, name):
        self.__real_name = name
    @real_name.deleter
    def real_name(self):
        print(f"deleted {self.__real_name}")
        del self.__real_name
    @property
    def family_members(self):
        return self.__family_members

    @family_members.setter
    def family_members(self, Members):
        self.__family_members = Members
    @family_members.deleter
    def family_members(self):
        print(f"deleted{self.__family_members}")
        del self.__family_members
class Hoghoghi(info):
    def __init__(self):
        super().__init__() 
        self.__fax_number = '00000000'
    
    @property
    def fax_number(self):
        return self.__fax_number
    @fax_number.setter
    def fax_number(self, fax):
        if len(fax) == 8:
            self.__fax_number = fax
        else:
            print("Invalid fax number format.")
    @fax_number.deleter
    def fax_number(self):
        print(f"deleted {self.__fax_number}")
        del self.__fax_number
class main:
    def __str__(self):
        return f'{self.ID}\t{self.Name}\t{self.code_city}{self.phone_number}\t{self.home_adress}\t{self.Email}'
    def __init__(self):
        self.haghighi_save = []
        self.hoghoghi_save = []
        self.code_ha = 999
        self.code_ho = 4999
        self.check_ha = 0
        self.check_ho = 1
        
        while True:
            system('cls')
            self.menu()
            n = input("enter your choice: ")
            match n:
                case '1':
                    x = input("1\thaghighi\n2\thoghoghi ")
                    match x:
                        case '1':
                           self.add_haghighi()
                        case '2':
                            self.add_hoghoghi()
                case '2':
                    x = input("1\thaghighi\n2\thoghoghi ")
                    match x:
                        case '1':
                            self.display_haghighi()
                        case '2':
                            self.display_hoghoghi()
                case '3':
                    search_by_id = str(input("enter the ID you wanna search for: "))
                    if search_by_id < '5000':
                        self.search_contact_by_id_haghighi(search_by_id)
                    elif search_by_id >= '5000':
                        self.search_contact_by_id_hoghoghi(search_by_id)
                case '4':
                    o = input("1\tclear all\n2\tclear with ID ")
                    if o == '1':
                        self.delete_all()
                    elif o == '2':
                        i = input("enter the idea you wanna delete: ")
                        self.delete_ID(i)
                    else:
                        input("invalid input")
                case '5':
                    x = input("1\thaghighi\n2\thoghoghi ")
                    match x:
                        case '1':
                            search_by_id = str(input("enter the ID you wanna edit: "))
                            self.search_contact_by_id_haghighi(search_by_id)
                            u = input("do you want to edit this ID? y/n")
                            if u == 'y' or 'Y':
                                self.edit_search_by_id_haghighi(search_by_id)
                            elif u =='n' or 'N':
                                pass
                            else:
                                print("invalid")
                        case '2':
                            self.search_contact_by_id_hoghoghi(search_by_id)
                            u = input("do you want to edit this ID? y/n")
                            if u == 'y' or 'Y':
                                self.edit_search_by_id_hoghoghi(search_by_id)
                            elif u =='n' or 'N':
                                pass
                            else:
                                print("invalid")
                    search_by_id = str(input('enter the ID you wanna edit'))
                    
    def check_email(self,email):
        email = email.upper()
        t = email.partition('@')
        state= False
        if t[0][0] == '@' or t[0][0] == '.' or t[0][-1] == '.':
            state = True
        for i in t[0]:
            if (i>'A' and i<'Z') or (i>'0' and i<'9') or i =='.':
                pass
            else:
                state = True
        if t[2].count('@')>0 or t[2].count('.')!=1 or t[2][0]=='.'or t[2][-1]=='.':
            state = True
        for i in t[2]:
            if (i>'A' and i<'Z') or (i>'0' and i<'9') or i == '.':
                pass
            else:
                state = True
        if not state:
            return True
    def menu(self):
        system('cls')
        print("1\tinsert info")
        print("2\tdisplay")
        print("3\tsearch by ID")
        print("4\tclear all data")
        print("5\tedit")
        print("6\tbreak")
    def add_hoghoghi(self):
        i = info()
        ho = Hoghoghi()

        self._check_ho = 1

        self.code_ho += 1
        self.hoghoghi_save.append(self.code_ho)

        new_name = input("Enter name: ")

        i.Name = new_name
        self.hoghoghi_save.append(i.Name)
        i.code_city = input("Enter code city: ")
        if len(i.code_city) != 3:
            print("Invalid code city number format.")
            return

        i.phone_number = input("Enter phone number: ")
        if len(i.phone_number) != 8 or not i.phone_number.isdigit():
            print("Invalid phone number format.")
            return

        i.home_adress = input("Enter your address: ")
        self.hoghoghi_save.append(i.home_adress)

        i.Email = input("Enter your email: ")
        bool_check = self.check_email(i.Email)
        if bool_check ==True:
            self.hoghoghi_save.append(i.Email)
        else:
            print("invalid email")

        ho.fax_number = input("Enter your fax number: ")
        self.hoghoghi_save.append(ho.fax_number)

        self.hoghoghi_save.append(i)
        print("Added successfully!")

        with open("d.txt", "a") as file:
            file.write(f"\n{self._check_ho},{self.code_ha},{i.Name},{i.code_city},{i.phone_number},{i.home_adress},{i.Email},{ho.fax_number}\n")
    
    def add_haghighi(self):
        i = info()
        ha = Haghighi()
        self.check_ha = 0

        self.code_ha += 1
        self.haghighi_save.append(self.code_ha)

        
        new_name = input("Enter name: ")

        i.Name = new_name
        self.haghighi_save.append(i.Name)
        i.code_city = input("Enter code city: ")
        if len(i.code_city) != 3:
            print("Invalid code city number format.")
            return

        i.phone_number = input("Enter phone number: ")
        if len(i.phone_number) != 8 or not i.phone_number.isdigit():
            print("Invalid phone number format.")
            return

        i.home_adress = input("Enter your address: ")
        self.haghighi_save.append(i.home_adress)

        i.Email = input("Enter your email: ")
        bool_check = self.check_email(i.Email)
        if bool_check ==True:
            self.haghighi_save.append(i.Email)
        else:
            print("invalid email")

        ha.family_members = input("Enter your family members: ")
        self.haghighi_save.append(ha.family_members)

        ha.real_name = input("Enter real name: ")
        self.haghighi_save.append(ha.real_name)

        self.haghighi_save.append(i)
        print("Contact added successfully!")

        with open("d.txt", "a") as file:  
            file.write(f"{self.check_ha},{self.code_ha},{i.Name},{i.code_city},{i.phone_number},{i.home_adress},{i.Email},{ha.family_members},{ha.real_name}\n")

    def display_hoghoghi(self):
        with open("d.txt", "r") as f:
            system('cls')
            display = f.readlines()
            print(f"{'ID':<6}{'Name':<20}{'Phone Number':<15}{'Home Address':<20}{'Email':<25}{"fax number":<8}")
            print(f"{'_'*121}")
            for j in display:
                temp = j.split(',')
                if temp[0] == '1':
                    print(f"{temp[1]:<6}{temp[2]:<20}{temp[3]:<15}{temp[4]:<20}{temp[5]:<25}{temp[6]:<8}")
        
            input(f"Press any key to continue{'.'*11}")

    def display_haghighi(self):
        with open("d.txt", "r") as f:
            system('cls')
            display = f.readlines()
            print(f"{'ID':<6}{'Name':<20}{'Phone Number':<15}{'Home Address':<20}{'Email':<25}{'Family Members':<15}{'Real Name':<20}")
            print(f"{'_'*121}")
            for j in display:
                temp = j.split(',')
                if temp[0] == '0':
                    print(f"{temp[1]:<6}{temp[2]:<20}{temp[3]:<15}{temp[4]:<20}{temp[5]:<25}{temp[6]:<15}{temp[7]:<20}")
        
            input(f"Press any key to continue{'.'*11}")
        
        print("Contact added successfully and saved to d.txt!")

    def search_contact_by_id_haghighi(self, search_id = 1000):
        with open("d.txt", "r") as f:
            display = f.readlines()
            for j in display:
                temp = j.split(',')
                if temp[1] == str(search_id):
                    print(f"{'ID':<6}{'Name':<20}{'Phone Number':<15}{'Home Address':<20}{'Email':<25}{'Family Members':<15}{'Real Name':<20}")
                    print(f"{'_'*121}")
                    print(f"{temp[0]:<6}{temp[1]:<20}{temp[3]:<15}{temp[4]:<20}{temp[5]:<25}{temp[6]:<15}{temp[7]:<20}")
        input("enter any buttons to continue")
    def search_contact_by_id_hoghoghi(self, search_id = 5000):
        with open("d.txt", "r") as f:
            display = f.readlines()
            for j in display:
                temp = j.split(',')
                if temp[1] == str(search_id):
                    print(f"{'ID':<6}{'Name':<20}{'Phone Number':<15}{'Home Address':<20}{'fax number':<8}")
                    print(f"{'_'*121}")
                    print(f"{temp[0]:<6}{temp[1]:<20}{temp[3]:<15}{temp[4]:<20}{temp[5]:<25}{temp[6]:<18}")
        input("enter any buttons to continue")
    def edit_search_by_id_haghighi(self, edit_id):
        with open("d.txt", "r") as f:
            display = f.readlines()

        for i,display in enumerate (display):
            temp = display.split(',')
            if temp[1] == str(edit_id):
                result = 0
                temp[0] = result
                result = temp[1]
                result = input("Enter new name: ")
                temp[2] = result
                result = input("Enter new city code: ")
                if len(result) == 3 and result.isdigit():
                    temp[3] = result
                else:
                    print("Invalid code city number format.")
                result = input("Enter new phone number: ")
                if len(result) == 8 and result.isdigit():
                    temp[4] = result
                else:
                    print("Invalid phone number format.")
                result = input("Enter new address: ")
                temp[5] = result
                result = input("Enter new email: ")
                temp[6] = result
                result = input("Enter new family members: ")
                temp[7] = result
                result = input("Enter new real name: ")
                temp[8] = result
                display[i] = ','.join(temp)+'\n'
            with open("d.txt", "w") as f:
                    f.writelines(display)
    def edit_search_by_id_hoghoghi(self, edit_id):
        with open("d.txt", "r") as f:
            display = f.readlines()

        for i,display in enumerate (display):
            temp = display.split(',')
            if temp[1] == str(edit_id):
                result = 0
                temp[0] = result
                result = input("Enter new name: ")
                temp[1] = result
                result = input("Enter new city code: ")
                if len(result) == 3 and result.isdigit():
                    temp[2] = result
                else:
                    print("Invalid code city number format.")
                result = input("Enter new phone number: ")
                if len(result) == 8 and result.isdigit():
                    temp[3] = result
                else:
                    print("Invalid phone number format.")
                result = input("Enter new address: ")
                temp[4] = result
                result = input("Enter new email: ")
                temp[5] = result
                result = input("Enter new fax number: ")
                temp[6] = result
                display[i] = ','.join(temp)+'\n'
            with open("d.txt", "w") as f:
                    f.writelines(display)
    def delete_all(self):
        with open("d.txt", "w") as f:
            pass
    def delete_ID(self,deleteId):
        with open("d.txt", "r") as f:
            lines = f.readlines()

        updated_lines = []

        for line in lines:
            temp = line.split(',')
            if temp[1] == str(deleteId):
    
                print(f"Deleting contact with ID {deleteId}: {temp[2]}")
            else:
                updated_lines.append(line)

        
        with open("d.txt", "w") as f:
            f.writelines(updated_lines)

        print("Contact deleted successfully!")
if __name__ == "__main__":
    main()
