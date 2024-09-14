class PersonalInfo:
    def __init__(self,name:str = "wasi",contact:str='03172175248',email:str='wasimuhmmad80@gmail.com',address:str='karachi'):
        self.__name = name
        self.__contact = contact
        self.__email = email
        self.__address = address

    def __repr__(self):
        return f'''personalinformation:
            name:{self.name} 
            contact:{self.contact}
            email:{self.email}
            address:{self.address}'''



    @property
    def name(self):
        return self.__name 


    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self.__name = value


    @property
    def contact(self):
        return self.__contact


    @contact.setter
    def contact(self,value):
        if isinstance(value,int):
            self.__contact = value



    @property
    def email(self):
        return self.__email


    @email.setter
    def email(self,value):
        if isinstance(value,str):
            self.__email = value    




    @property
    def address(self):
        return self.__address


    @address.setter
    def address(self,value):
        if isinstance(value,str):
            self.__address = value

if __name__ == "__main__":
    personalInfo = PersonalInfo('Suhaib ahmed','03111066388','khansuhaibahmed902@gmail.com','karachi')
    print(personalInfo)    