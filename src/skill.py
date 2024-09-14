class Skills:
    def __init__(self,name:str,level:str=['basic','intermediate','advance']):
        self.name=name
        self.level=level
      

    def __repr__(self):
        return f'''Skills :
            name:{self.name} 
            level:{self.level}'''

    @property
    def name(self):
        return self.__name 


    @name.setter
    def name(self,value):
        if isinstance(value,str):
            self.__name = value


    @property
    def level(self):
        return self.__level


    @level.setter
    def level(self,value):
        if isinstance(value,str):
            self.__level = value



if __name__ == "__main__":
    skill = Skills('python,html,typescript,css','basic')
    print(skill)    

